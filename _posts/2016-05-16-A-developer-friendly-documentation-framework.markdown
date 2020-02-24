---
layout: post
title:  "reSt Docs - A developer friendly documentation framework!"
date:   2016-05-16 10:31:02 -0500
categories: ideas
---

## Everybody knows the value of having a very 
 - Well Structured
 - Consistently formatted
 - Multimodal (PDF/HTML/DOC/Epub etc)
 - Searchable by default
 - EASY to author and publish

As a software architect the one golden thumb rule I follow is... 

> When in doubt …ask yourself..."What would the open source community do?" -- mm Rule#1

# 1. Docs in the wild!

Docs in the Wild! Have you come across this?

![Popular documentation formats in internet]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework-all-0.png){:class="img-responsive"}

- #### Consistent formatting

![Documentation formatting]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework4.png){:class="img-responsive"}
  
![Documentation code highlighting]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework5.png){:class="img-responsive"}

- #### Searchable
  
![Documentation search feature]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework6.png){:class="img-responsive"}

- #### Multi Modal plugins

![multi modal example]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework7.png){:class="img-responsive"}

# 2. reST– Intro (spoiler alert…it’s a markdown language)

reSt (restructuredText)

My first thought like yours :

Please Don’t tell me  I have to learn yet  another  markdown  language!!!!!

Yes you do!

But relax!!!  It’s surprisingly easy  markdowns  You will see

reSt  ructuredText  :  e:g

  * Full reference @ http://docutilssourceforgenet/docs/user/rst/quickstarthtml

# 3. Sphinx

- Does all the heavy lifting.
- Runs under python.
- Provides additional non-reSt markdown.
- Can be embedded right into your project folder path.
- Most importantly provides the ubiquitous sphinx_rtd_theme theme.
  - Refer @ http://www.sphinx-doc.org/en/stable/tutorial.html

![Sphinx embed into project]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework9.png){:class="img-responsive"}

# 4. Getting started with Sphinx:

- Step 1: Install Sphinx using python package manager [install sphinx](https://www.sphinx-doc.org/en/master/index.html)
  
    $ pip install Sphinx

- Step 2: Once installed, use the quick start option to quickly generate a project [quickstart](https://www.sphinx-doc.org/en/master/usage/quickstart.html)


    $ sphinx quickstart

- Step 3: Include project into your source code in eclipse (optional)

- Step 4: Update the configuration: Confpy:

Import the sphinx_rtd_theme and set the html_theme in confpy

![Documentation]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework10.png){:class="img-responsive"}

- Step 5: Build a TOC tree:

Index.rst is usually the best place to start placing your topic toclinks

![Documentation]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework11.png){:class="img-responsive"}

You can include external images using figure  :: markdown

![Documentation]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework12.png){:class="img-responsive"}

- Step 6: Build the docs with sphinx build

![Documentation]({{site.baseurl}}/assets/images/doc-framework/Documentation_Framework13.png){:class="img-responsive"}

# 5. Other considerations

* Doc lives like any other the code:
  * The reST docs should live like a code and follow the same release life cycle We would have to
* Continuous Integration:
  * Because we have a build script,  it is easy to rebuild the document changes after every release (assuming the developer has updated the docs)
* Versioning:
  * There are sphinx extensions available for handling this mainly using git (e:g  sphinxcontrib -versioning, Find more @ [sphinx versioning](https://github.com/sphinx-contrib/sphinxcontrib-versioning)
* Hosting / Deployment:
  * The Sphinx build output is just a bunch of static html pages pdf, which could be hosted on any of our light weight http server



