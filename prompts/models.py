from django.db                  import models
from django.conf                import settings
from django.urls                import reverse
from rest_framework.reverse     import reverse as api_reverse


# Create your models here.
class Genre(models.Model):
    # Hidden: PK or id. This is auto generated by django when making models
    genre_name  = models.CharField(max_length=256, null=False, blank=False)
    parent_id   = models.ForeignKey("self", null=True, blank=True)

    def __str__(self):
        return str(self.genre_name)


class PieceType(models.Model):
    # Hidden: PK or id. This is auto generated by django when making models
    piece_type_name = models.CharField(max_length=256, null=True)

    def __str__(self):
        return str(self.piece_type_name)


class PromptPiece(models.Model):
    # Hidden: PK or id. This is auto generated by django when making models
    piece_type          = models.ForeignKey(PieceType, on_delete=models.CASCADE)
    piece_genre         = models.ForeignKey(Genre, on_delete=models.CASCADE)
    piece_name          = models.CharField(max_length=256, null=False, blank=False)
    piece_description   = models.TextField(max_length=256, null=True, blank=True)

    def get_random_by_genre(self):
        pass

    def __str__(self):
        return str(self.piece_name)


class BuiltPrompt(models.Model):
    prompt_name     = models.CharField(max_length=256, null=True, blank=True)
    prompt_person   = models.ForeignKey(PromptPiece, null=False, blank=False, related_name='prompt_person')
    prompt_place    = models.ForeignKey(PromptPiece, null=False, blank=False, related_name='prompt_place')
    prompt_thing    = models.ForeignKey(PromptPiece, null=False, blank=False, related_name='prompt_thing')
    prompt_scenario = models.ForeignKey(PromptPiece, null=False, blank=False, related_name='prompt_scenario')

    def __str__(self):
        return str(
            self.prompt_name    + "\n\n " +
            "\tPerson:\t\t\t"    + self.prompt_person.piece_name     + " \n " +
            "\tPlace:\t\t\t"     + self.prompt_place.piece_name      + " \n " +
            "\tThing:\t\t\t"     + self.prompt_thing.piece_name      + " \n " +
            "\tScenario:\t\t"  + self.prompt_scenario.piece_name
        )





