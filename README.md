# mkdocs-edupress-theme
Edupress theme for mkdocs.

Recommend installing mkdocs-paginate-plugin for best results.

Example from this project: https://kubilus1.github.io/mkdocs-edupress-theme/

# Layout

This is intended for a typical blog style layout.  A top level 'index.md' is
expected, but basically ignored.  Posts can be in a subdir or in the top level
directory.  All files will be collected and treated as posts.

# Extras

This theme supports a few special yaml config items in your posts such as:

```
index: <int> 
```

This allows you to control the layout of posts.  These will be sorted in
reverse order.  As you add new posts you can expect the greatest number/newest
to be first.

```
featured_image: <path>
```

Adds a featured image to a post.  This should be relative to the top level of
the site_url.  Leave off any beginning `/`

```
tags: [<list of tags>]
```

Adds lists of tags on the homepage for each post.  This may be used at a later
point to show pages of matching tags.

```
author: <name>
```

Show the post's author.  This may be used in the future to provide a page of
matching articles.

```
date: <date>
```

Show the date of a post.
