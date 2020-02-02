from jsonmodels import models, fields, errors, validators
from enum import Enum


class GroupKey(models.Base):
    text = fields.StringField(required=True)


class GroupKeyShortLabel(models.Base):
    sequenceNumber = fields.FloatField(required=True)


class Grouping(models.Base):
    groupKey = fields.EmbeddedField(GroupKey, required=True)
    groupKeyShortLabel = fields.EmbeddedField(GroupKeyShortLabel, required=True)
    explanation = fields.ListField([fields.StringField()], required=True)
    debug = fields.EmbeddedField([fields.StringField()], required=True)
    dateTime = fields.DateTimeField(required=True)


class TitleType(Enum):
    MANIFESTATION = 1
    TRANSLATED = 2
    FORMER = 3
    VARIANT = 4
    ABBREVIATED = 5
    KEY = 6
    WORK = 7
    HOLDING = 8


class Script(Enum):
    ARABIC = 1
    LATIN = 2
    CHINESE_JAPANESE_KOREAN = 3
    CYRILLIC = 4
    GREEK = 5
    HEBREW = 6


class OtherScriptRepresentation(models.Base):
    content = fields.StringField()
    script = fields.EmbeddedField(Script)


class Title(models.Base):
    titleType = fields.EmbeddedField(TitleType, required=True)
    mainTitle = fields.StringField(required=True)
    mainTitleOtherScript = fields.ListField([OtherScriptRepresentation])
    subTitle = fields.StringField()
    subTitleOtherScript = fields.ListField([OtherScriptRepresentation])
    displayTitle = fields.StringField(required=True)
    displayTitleOtherScript = fields.ListField([OtherScriptRepresentation])


class Relationship(models.Base):
    relationship = fields.StringField(required=True)


# TODO: make a general URI field? (does python have an available URI type?)
class RelationshipURI(models.Base):
    uri = fields.StringField()


class Name(models.Base):
    nameType = fields.StringField(name='type')
    fullName = fields.StringField(required=True)
    displayName = fields.StringField(required=True)
    firstLastForm = fields.StringField()
    initialisms = fields.ListField(fields.StringField())
    otherScriptFullName = fields.ListField([OtherScriptRepresentation])
    otherScriptDisplayName = fields.ListField(fields.StringField())


class Creator(models.Base):
    name = fields.StringField(required=True)
    creatorURI = fields.StringField()
    relationships = fields.ListField(Relationship, required=True)
    relationshipURIs = fields.ListField(RelationshipURI)
    accessPoint = fields.StringField(required=True)
    otherNames = fields.ListField([Name])
    localAuthorityURI = fields.StringField()


class PublicationInfoType(Enum):
    PRODUCTION = 1
    PUBLICATION = 2
    DISTRIBUTION = 3
    MANUFACTURE = 4
    COPYRIGHT = 5


class PublicationData(models.Base):
    location = fields.ListField([fields.StringField()])
    name = fields.StringField(nullable=True)
    date = fields.StringField(nullable=True)
    isInexact = fields.BoolField(nullable=True)


class PublicationInformation(models.Base):
    type = fields.EmbeddedField(PublicationInfoType, required=True)
    statement = fields.StringField(required=True)
    isCurrentPublisher = fields.BoolField(required=True)
    publicationData = fields.EmbeddedField(PublicationData)


class IdentifierType(Enum):
    ISBN = 1
    ISSN = 2
    LINKED_ISSN = 3
    UPC = 4
    LCCN = 5
    OCLC = 6
    NUCMC = 7
    ISRC = 8
    ISMN = 9
    SYSTEM = 10
    GPO_NUMBER = 11
    REPORT_NUMBER = 12
    EAN = 13
    SICI = 14
    ISSUE_NUMBER = 15
    MATRIX_NUMBER = 16
    PLATE_NUMBER = 17
    PUBLISHER_NUMBER_MUSIC = 18
    PUBLISHER_NUMBER_VIDEO = 19
    PUBLISHER_NUMBER_AV = 20
    DISTRIBUTOR_NUMBER_AV = 21
    ASIN = 22


class Status(Enum):
    VALID = 1
    INCORRECT = 2
    CANCELLED = 3


class Identifier(models.Base):
    value = fields.StringField(required=True)
    displayForm = fields.StringField(required=True)
    type = fields.EmbeddedField(IdentifierType, required=True)
    status = fields.EmbeddedField(Status, required=True)


class Review(models.Base):
    providerURI = fields.StringField(required=True)
    contents = fields.StringField(required=True)
    source = fields.StringField()
    reviewLink = fields.StringField()
    reviewDate = fields.StringField()
    fullDetailsURI = fields.StringField()


class Summary(models.Base):
    providerURI = fields.StringField(required=True)
    contents = fields.StringField(required=True)
    source = fields.StringField()


class EditionStatement(models.Base):
    edition = fields.StringField(required=True)


class ImageType(Enum):
    LOCAL = 1
    NONLOCAL = 2


class CoverImageInfo(models.Base):
    imageType = fields.EmbeddedField(ImageType)
    providedURI = fields.StringField()
    smallImageLink = fields.StringField()
    mediumImageLink = fields.StringField()
    largeImageLink = fields.StringField()


class Format:
    pass  # This is actually just a single value, not duping the Core format enum here for now


class Language:
    pass  # This is actually just a string atm...


class AuthorNote(models.Base):
    notes = fields.StringField(required=True)
    providerURI = fields.StringField(required=True)


class BibliographicLevel(Enum):
    WORK = 1
    INSTANCE = 2
    ITEM = 3


class ResourceComponent(models.Base):
    componentTitle = fields.EmbeddedField(Title, required=True)
    contributor = fields.EmbeddedField(Creator)
    description = fields.StringField()
    bibliographicLevel = fields.EmbeddedField(BibliographicLevel)


# No Contributor class; it's the same as Creator


class Excerpt(models.Base):
    excerpt = fields.StringField(required=True)
    providerURI = fields.StringField(required=True)


class CallNumberType(Enum):
    LCCN = 1
    UDC = 2
    DDC = 3
    LAC = 4
    NLM = 5
    NAL = 6  # National Agricultural Library
    GOVDOC = 7
    LOCAL = 8
    LOCAL_LCCN = 9
    LOCAL_DDC = 10


class CallNumber(models.Base):
    type = fields.EmbeddedField(CallNumberType, required=True)
    value = fields.StringField(required=True)


class Note(models.Base):
    note = fields.StringField(required=True)
    otherResourceURLs = fields.ListField(fields.StringField())
    otherResourceIdentifiers = fields.ListField(Identifier)
    appliesToResourcePart = fields.StringField()
    marc21NoteType = fields.StringField()


class SubjectType(Enum):
    AGENT = 1  # e.g. a real person, corporation, etc.
    TITLE = 2
    PLACE = 3
    CHARACTER = 4
    CHRONOLOGY = 5
    GENERAL = 6
    INDEX_TERM = 7  # TODO, might want to move this to its own element in a later iteration. - HZ, 08/22/19


class Subject(models.Base):
    type = fields.EmbeddedField(SubjectType, required=True)
    heading = fields.StringField(required=True)
    mainTerm = fields.StringField(required=True)
    otherTopics = fields.ListField(fields.StringField())
    forms = fields.ListField(fields.StringField())
    chronologies = fields.ListField(fields.StringField())
    places = fields.ListField(fields.StringField())
    relationship = fields.StringField()


class Genre(models.Base):
    heading = fields.StringField(required=True)
    mainTerm = fields.StringField(required=True)
    otherTopics = fields.ListField(fields.StringField())
    forms = fields.ListField(fields.StringField())
    chronologies = fields.ListField(fields.StringField())
    places = fields.ListField(fields.StringField())


class ExternalResource(models.Base):
    title = fields.StringField()
    description = fields.StringField()
    appliesToResourcePart = fields.StringField()
    resourceURIs = fields.ListField(fields.StringField())  # is this correct?


class SeriesInfo(models.Base):
    title = fields.EmbeddedField(Title, required=True)
    contributors = fields.ListField(Creator)
    volume = fields.StringField()
    identifier = fields.ListField(Identifier)
    linkedForSearch = fields.BoolField(required=True)
