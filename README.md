# Django for Atom

[![Greenkeeper badge](https://badges.greenkeeper.io/zacharytamas/atom-django.svg)](https://greenkeeper.io/)

> Build Django apps faster with Atom.

## Install

```bash
$ apm install atom-django
```

Or Settings ➔ Install ➔ Search for `atom-django`

## Features

### Snippets

This plugin features several snippets to help you write boilerplate code faster, mostly for writing out models' Fields. These snippets also have preset insertion points that let you tab between various parts of the snippet that you likely want to change. These are noted in the snippets below as `$1`, `$2`, and so on. Occasionally these have default values inside them such as `${1:default value}`.

#### Basic model skeleton

`model` becomes:

    class ${1:Modelname}(models.Model):
        """${2:($1 description)}"""
        $0
        def __unicode__(self):
            return u"$1"

#### `AutoField`

`auto` becomes:

  `${1:FIELDNAME} = models.AutoField()`

#### `BooleanField`

`boolean` becomes:

  `${1:FIELDNAME} = models.BooleanField(${2:default=True})`

#### `CharField`

`char` becomes:

  `${1:FIELDNAME} = models.CharField(${2:blank=True}, max_length=${3:100})`

#### `CommaSeparatedIntegerField`

`commaseparatedinteger` becomes:

  `${1:FIELDNAME} = models.CommaSeparatedIntegerField(max_length=$2)`

#### `DateField`

`date` becomes:

  `${1:FIELDNAME} = models.DateField(${2:default=datetime.datetime.today})`

#### `DateTimeField`

`datetime` becomes:

  `${1:FIELDNAME} = models.DateTimeField(${2:blank=True}${3:, default=datetime.datetime.now})`

#### `DecimalField`

`decimal` becomes:

  `${1:FIELDNAME} = models.DecimalField(max_digits=$2, decimal_places=$3)`

#### `EmailField`

`email` becomes:

  `${1:FIELDNAME} = models.EmailField()`

#### `FileField`

`file` becomes:

  `${1:FIELDNAME} = models.FileField(upload_to=${1:/path/for/upload})`

#### `FilePathField`

`filepath` becomes:

  `${1:FIELDNAME} = models.FilePathField(path="${1:/location/of/choices}"${2:, match="${3:regex}"}${4:, recursive=True})`

#### `FloatField`

`float` becomes:

  `${1:FIELDNAME} = models.FloatField()`

#### `ForeignKey`

`fk` becomes:

  `${1:FIELDNAME} = models.ForeignKey(${2:RELATED_MODEL})`

#### `IPAddressField`

`ipaddress` becomes:

  `${1:FIELDNAME} = models.IPAddressField(${2:blank=True})`

#### `ImageField`

`image` becomes:

  `${1:FIELDNAME} = models.ImageField(upload_to="${2:/dir/path}"${3:, height_field=$4}${5:, width_field=$6})`

#### `IntegerField`

`integer` becomes:

  `${1:FIELDNAME} = models.IntegerField(${2:blank=True, null=True})`

#### `ManyToManyField`

`manytomany` becomes:

  `${1:FIELDNAME} = models.ManyToManyField(${2:RELATED_MODEL})`

#### `NullBooleanField`

`nullboolean` becomes:

  `${1:FIELDNAME} = models.NullBooleanField(${2:default=True})`

#### `PhoneNumberField`

`phonenumber` becomes:

  `${1:FIELDNAME} = models.PhoneNumberField(${2:blank=True})`

#### `PositiveIntegerField`

`positiveinteger` becomes:

  `${1:FIELDNAME} = models.PositiveIntegerField(${2:blank=True, null=True})`

#### `PositiveSmallIntegerField`

`positivesmallinteger` becomes:

  `${1:FIELDNAME} = models.PositiveSmallIntegerField(${2:blank=True, null=True})`

#### `SlugField`

`slug` becomes:

  `${1:slug} = models.SlugField()`

#### `SmallIntegerField`

`smallinteger` becomes:

  `${1:FIELDNAME} = models.SmallIntegerField(${2:blank=True, null=True})`

#### `TextField`

`text` becomes:

  `${1:FIELDNAME} = models.TextField(${2:blank=True})`

#### `TimeField`

`time` becomes:

  `${1:FIELDNAME} = models.TimeField(${2:blank=True})`

#### `URLField`

`url` becomes:

  `${1:FIELDNAME} = models.URLField(${2:blank=True})`

#### `USStateField`

`usstate` becomes:

  `${1:FIELDNAME} = models.USStateField(${2:blank=True})`

#### `XMLField`

`xml` becomes:

  `${1:FIELDNAME} = models.XMLField(schema_path=${2:/path/to/RelaxNG}${3:, blank=True})`

#### `send_mail`

`sendmail` becomes:

    mail.send_mail("${1:Subject}", "${2:Message}", "${3:from@example.com}", ${4:["to@example.com"]}${5:, fail_silently=True})

## Release Notes

### 0.3.1

* Fix a [syntax highlighting bug](https://github.com/zacharytamas/atom-django/issues/9).

### 0.1.0

* Initial build of Django for Atom.
* At the moment it is merely a clone of the superb [Django TextMate bundle](https://github.com/textmate/python-django.tmbundle) but new content may be added in the future.

## License

MIT © [Zachary Jones](http://github.com/zacharytamas)
