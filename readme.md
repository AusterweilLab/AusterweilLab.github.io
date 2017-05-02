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

Like in the people page, you should be able to add/edit lab papers using a json file: `_data/papers.json`. The html for this page is a bit more complex because I had to construct citations on the fly and add abstract toggling and tag functions, but you should be able to add and edit pages exclusively in the json file.

Things to note:

1. Locally hosted PDFs are stored in `papers/files/`
2. My code is _very_ picky about the formatting of the data. If you have missing fields, or punctuation where I did not expect punctuation, or anything else that I did not think of, your citation will look terrible. I would recommend copying an existing citation very closely because my implementation is not at all robust.
3. If you use a new tag, you'll need to specify its color in `_data/tagcolors.json`. I have been using the [Material Theme Colors](https://material.io/guidelines/style/color.html), and I've listed some unused ones in the comments of that file. Just add an entry for your tag with the color you want.
4. Right now the only supported paper types are `"article-journal"`, `"paper-conference"` and `"chapter"` because, again, my implementation is not at all robust.

## How to make a new project page.

### Syntax highlighting and MathJax.

## How to add a news post.

