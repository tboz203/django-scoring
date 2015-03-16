# django-scoring models
# author: tboz203
# date: 2015-03-12

from django.db import models
from django.core.validators import RegexValidator


class Manager(models.Model):
    '''
    Represents the manager of a team. A single manager may be responsible for
    multiple teams. Holds a name and a phone number.
    '''
    name = models.CharField(max_length=128, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=(
            "Phone number must be entered in the format: " +
            "+999999999 Up to 15 digits allowed."))
    # validators should be a list
    phone_number = models.CharField(validators=[phone_regex], blank=True,
            max_length=15)

    class Meta:
        ordering = ['name']
        verbose_name = 'Team Manager'

    def  __str__(self):
        return self.name


class School(models.Model):
    '''
    Represents a school. Multiple teams can come from the same school. Holds a
    name.
    '''
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ['name']

    def  __str__(self):
        return self.name


class TeamChallenge(models.Model):
    '''
    Represents a team challenge. One team challenge will have many appraisers
    and events (performances), and will have a number of scoring fields
    associated with it. Holds a name.
    '''
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Team Challenge'

    def __str__(self):
        return self.name


class Location(models.Model):
    '''
    Represents a location at the tournament. One location will have several
    events. Holds a name.
    '''
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Team(models.Model):
    '''
    Represents a team competing at the tournament. A team will have one team
    challenge event and one instant challenge event. Holds a name and a
    classification, and references a manager and a school.
    '''
    ELEMENTARY = 'E'
    MIDDLE = 'M'
    HIGH = 'H'
    UNIVERSITY = 'U'
    OTHER = 'O'
    CLASIFICATION_CHOICES = (
            (ELEMENTARY, 'Elementary'),
            (MIDDLE, 'Middle'),
            (HIGH, 'High'),
            (UNIVERSITY, 'University'),
    )

    name = models.CharField(max_length=128, unique=True)
    classification = models.CharField(max_length=1,
            choices=CLASIFICATION_CHOICES)
    manager = models.ForeignKey(Manager)
    school = models.ForeignKey(School)
    team_challenge = models.ForeignKey(TeamChallenge)

    class Meta:
        ordering = ['classification', 'name']

    def __str__(self):
        return self.name


class TC_Field(models.Model):
    '''
    Represents a field on a team challenge scoring form (unique per team
    challenge). A scoring field will have one score per event per appraiser
    assigned to it. Holds a name and a field type, and a reference to a team
    challenge.
    '''
    name = models.CharField(max_length=128, unique=True)
    field_type = models.IntegerField()
    team_challenge = models.ForeignKey(TeamChallenge)

    class Meta:
        ordering = ['team_challenge', 'name']
        verbose_name = 'Team Challenge Scoring Field'

    def __str__(self):
        return self.name


class TC_Appraiser(models.Model):
    '''
    Represents a team challenge appraiser. An appraiser will have one score per
    event they appraise per field assigned to them. Holds a name, and a reference to a team
    challenge.
    '''
    name = models.CharField(max_length=128, unique=True)
    team_challenge = models.ForeignKey(TeamChallenge)

    class Meta:
        ordering = ['name']
        verbose_name = 'Team Challenge Appraiser'

    def __str__(self):
        return self.name


class TC_Event(models.Model):
    '''
    Represents a team challenge event (performance). One event will have a
    number of scores associated with it. Holds a time, and references a team, a team
    challenge, and a location.
    '''
    time = models.DateTimeField()
    team = models.ForeignKey(Team, unique=True)
    team_challenge = models.ForeignKey(TeamChallenge)
    location = models.ForeignKey(Location)

    class Meta:
        ordering = ['time']
        verbose_name = 'Team Challenge Event'


class TC_Score(models.Model):
    '''
    Represents a single score in a field for a team challenge event. Holds a
    value, and references a scoring field, an event, and an appraiser.
    '''
    value = models.CharField(max_length=32)
    tc_field = models.ForeignKey(TC_Field)
    tc_event = models.ForeignKey(TC_Event)
    tc_appraiser = models.ForeignKey(TC_Appraiser)

    class Meta:
        verbose_name = 'Team Challenge Score'

    def __str__(self):
        return self.value


class IC_Appraiser(models.Model):
    '''
    Represents an instant challenge appraiser. An appraiser will have a single
    score per event they appraise. Holds a name.
    '''
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Instant Challenge Appraiser'

    def __str__(self):
        return self.name


class IC_Event(models.Model):
    '''
    Represents a single instant challenge event. An instant challenge will have
    one score per appraiser appraising it. Holds a time, and references a team
    and a location.
    '''
    time = models.DateTimeField()
    team = models.ForeignKey(Team, unique=True)
    location = models.ForeignKey(Location, unique=True)

    class Meta:
        ordering = ['time']
        verbose_name = 'Instant Challenge Event'


class IC_Score(models.Model):
    '''
    Represents a single appraiser's score for an instant challenge. Holds a
    value, and references an event and an appraiser.
    '''
    # same as for TC_Score.value
    value = models.CharField(max_length=32)
    ic_event = models.ForeignKey(IC_Event)
    ic_appraiser = models.ForeignKey(IC_Appraiser)


    class Meta:
        ordering = ['ic_event']
        verbose_name = 'Instant Challenge Score'

    def __str__(self):
        return self.value

# --------------------
# meta fields (i guess?)
# --------------------

class TC_Appraiser_Permission(models.Model):
    '''
    Represents a requirement for a specific appraiser to enter a score into a
    specific scoring field. Holds a reference to an appraiser and a tc scoring
    field.
    '''
    tc_appraiser = models.ForeignKey(TC_Appraiser)
    tc_field = models.ForeignKey(TC_Field)

    class Meta:
        ordering = ['tc_appraiser']
        verbose_name = 'Team Challenge Appraiser Permission'


# class TC_Appraiser_Role(models.Model):
#     '''
#     Represents a collection of appraiser permissions that ... hrmmm
#     '''
#     pass
