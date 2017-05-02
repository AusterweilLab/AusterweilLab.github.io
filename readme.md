# Jekyll-Based Lab Website

This page will provide some info on how to edit and deploy the lab website.



## How does Jekyll work?

[Jekyll](https://jekyllrb.com/) is a content management system for building static sites with a blog functionality. Basically, you edit code within Jekyll's framework, and Jekyll will automatically create a static site to your specification. This is really useful because you can programatically use things like html snippets, json data, etc, rather than hard-coding everything you need into each index page.

So to edit the website, you'll need to install Jekyll. I'm not going to write a whole tutorial on how it works, but there are lots of good ones online. Instead, I'll write some quick instructions on how to edit specific information.

To edit _anything_, you'll want to be running the Jekyll service in the background. So after you've downloaded the code and installed Jekyll (you'll also need ruby, ruby gems, and the gem bundler), you can install the packages we use for the page to your computer via:


```ruby
bundle install
```

You only need to do that once, unless you start using other packages. Then you can run the service with

```ruby
bundle exec jekyll serve 
```

Or just `jekyll serve`. Jekyll will then compile the website into a subdirectory (`_site/`) and you can visit it on localhost (`http://127.0.0.1:4000/`). Jekyll will monitor the files for changes, and will automatically recompile the website whenever you save a change. So just run that command and then you're good to go.

After you've made changes, you can just copy the contents of `_site/` into the root of our webserver and the site _should_ work. 


## How to edit the lab members page.

Joe will probably ask for this to be done every year or so. The people page is in `people/index.html`, so you'll be editing that file (you will _not_ edit `_site/people/index.html`). You'll see that Jekyll's [Liquid](https://gist.github.com/smutnyleszek/9803727) Syntax is in use: anything inside of `{% ... %}` and `{{ ... }}`  is interpreted as Liquid and you can use that to make pages more dynamic.

I have stored all the information about lab members in a special directory: `_data/people.json`. This file contains all the information relating to lab members, and if you only want to add/remove people, you'll only need to edit this file. You can delete / move people between categories, and you can also add entirely new categories and the thing should work. The fields are pretty straightforward so there's not much to talk about here. If you don't specify a particular image, Larry David is used.

You can also see that I apply special CSS at the bottom of each page. That's just good to know if you can't figure out where in `css/style.css` a styling is applied.


## How to add a new paper.

Like in the people page, you should be able to add/edit lab papers using a json file: `_data/papers.json`. The html for this page is a bit more complex because I had to construct citations on the fly and add abstract toggling and tag functions, but you should be able to add and edit papers exclusively in the json file.

Things to note:

1. Locally hosted PDFs are stored in `papers/files/`
2. My code is _very_ picky about the formatting of the data. If you have missing fields, or punctuation where I did not expect punctuation, or anything else that I did not think of, your citation will look terrible. I would recommend copying an existing citation very closely because my implementation is not at all robust.
3. If you use a new tag, you'll need to specify its color in `_data/tagcolors.json`. I have been using the [Material Theme Colors](https://material.io/guidelines/style/color.html), and I've listed some unused ones in the comments of that file. Just add an entry for your tag with the color you want.
4. Right now the only supported paper types are `"article-journal"`, `"paper-conference"` and `"chapter"` because, again, my implementation is not at all robust.

## How to make a new project or news page.

If you are writing a new project or news page, to eventually be listed in `projects/` or in the news marquee, you'll need to write it in markdown. I am using Jekyll's blog functionality to handle these items, and so all posts are markdown files within the `_posts\` directory. For organization, I have split that directory into `news` and `projects` subdirectories.

In either case, the markdown files are specially formatted, with YAML frontmatter at the very beginning. Liquid syntax can also be used in these posts, in case you were wondering.

Here is a sample news post:

```
---
title: The title of the news post.
excerpt: A sentence or two about the news.
tags: tags, for, seo
layout: post
category: news
---

Some other content can go here! This will be visible to 
whoever clicks the link in the news post.
```

News posts in particular can be exclusively the YAML front matter, but they don't have to be.

Here's what the front matter items do:

| Field          | Description                                     |
| -------------- | ----------------------------------------------- |
| `title` | For news, this is the text that is shown on the main page.  For projects, this will be the title of the project. |
| `excerpt` | This is set as the page meta description for SEO, but it might also come in handy if we ever need a quick abstract about the post. |
| `tags` | These are also used for SEO, but are additionally shown below the title of the page when you click the link to the post, so make sure they are appropriate. |
| `layout` | This references a specific HTML layout that I have written. It should always be the name of a file in `_layouts`. The one i have written, `post`, is very general and you shouldn't need to write a new one. |
| `category` |  This will either be `news` or `projects`, depending on which you are writing.|

The file also has to be named very particularly for Jekyll to interpret it. Here is how it should look:

```
YYYY-M-DD-short-name.md
```

The date listed in that file will be shown on the post page, and also it will affect its order in the news marquee (which only shows the most recent three posts, in order of recency). So make sure that's done correctly!

### Syntax highlighting, MathJax, and Tables

I have additionally enabled syntax highlighting and MathJax on post pages, and I've written some special table styling. Here's how you use these things:

#### Syntax highlighting

Syntax highlighting works as with any Github-flavored markdown:

    ```python
    for i in range(3):
        print(i)
    ```

That would produce this highlighting:

```python
for i in range(3):
    print(i)
```

This [page](https://github.com/jneen/rouge/wiki/List-of-supported-languages-and-lexers) lists the languages that Jekyll's default highlighter, rouge, _should_ know about.

#### MathJax

By default MathJax is not loaded because it is a big library, so if you want to use it you will need to include this line in your YAML frontmatter:

```
use_math: true
```

If that line is in there, the MathJax library will be loaded. After you do that, you can use inline and display math like so:

```
This sentence has some inline math: \\(y=mx+b\\)
```

```
Hey, check out this display equation:

$$
e = mc^2
$$
```

I do not know a lot about MathJax and I constantly need to look things up, but i know those two things work! I would suggest constant checking to make sure your math displays correctly.

#### Tables

The default markdown table styling is _garbage_, so I have written special styling to make tables look nicer. To activate the styling, you need to apply a CSS class (`.datatable`) by using a decorator:

```
My great markdown table:

{:.datatable}
| Column 1 | Column 2 | 
| -------- | -------- |
| This |  Table |
| Looks | Great! |
```


Putting all of that together, here's an example of a  project post:

    ---
    title: This is a sample project page!
    excerpt: A description. Maybe a sentence or two.
    tags: tags,for,seo
    layout: post
    category: projects
    use_math: true
    ---
    
    Some introduction, blah blah blah. Here is some code:
    
    ```python
    def BagelBites(time):
        if time.lower() in ['morning','evening','suppertime']:
            return('Pizza')
        else:
            raise Exception('When pizza\'s on a bagel, you can have pizza anytime!')
    ```
    
    My special inline math: \\(y=mx+b\\)
    
    My special display math:
    
    $$
    e = mc^2
    $$
    
    And, hey, look at this table!
    
    {:.datatable}
    | Column 1 | Column 2 | 
    | -------- | -------- |
    | This |  Table |
    | Looks | Great! |
