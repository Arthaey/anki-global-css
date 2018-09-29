# Description

Anki download ID:  FIXME

An Anki add-on to keep all notes' CSS in sync with an external styleshet file.
This is useful if you want to have the same CSS shared between your models,
*and* you want the CSS available on mobile (where `@import &lt;file&gt;` doesn't
work).

It replaces all models' templates with the contents of your stylesheet file
on startup. If you make changes to your file, use the "Update global CSS" menu
item or restart Anki for them to take effect.

# Requirements

- a file named `_global.css` in your profile's `collection.media` directory

# Support

Post a [new issue on Github](https://github.com/Arthaey/anki-global-css/issues/new)
(or make a pull request!). You can also write a review or ask questions on the
[Anki website for shared add-ons](https://ankiweb.net/shared/info/). FIXME

[My other Anki add-ons](https://github.com/search?q=user%3AArthaey+anki)
are also on Github.

# License

This addon is licensed under the same license as Anki itself(GNU Affero General
Public License 3).
