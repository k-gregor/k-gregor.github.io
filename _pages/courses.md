---
layout: page
title: courses
nav: true
permalink: /courses/
---

I offer various courses distilling the most important aspects of software engineering for scientific groups.
Courses can be in-person or online, and they usually consist of a presentation part and a workshop part, but can be fully customized to your needs.
I have so far given courses at:

- Technical University of Munich
- University of California, Berkeley

Do not hesitate to reach out and we can discuss potential courses for your group! Just write me an [e-mail](mailto:konstantin.gregor@posteo.de).

# Topics

The topics of the courses can be adjusted to your particular needs. 
From my experience, the `Best practices for coding in science` and `Fundamentals of data science` courses are highly useful for most research groups. Even though it is mostly a presentation, is it still interactive, with quizzes and small tasks.
The other courses contain both presentation and hands-on workshop parts.

But generally, we can adapt the courses as you need, as potentially not all aspects will be relevant for your group. Here are some general courses that I have taught:

<br/>

# Courses

- Fundamentals of data science
- Fundamentals of programming in Python
- Best practices for programming for scientists
- Version control with `git` for scientists
- Monitoring and optimizing resource usage of scientific code
- Making quantitative research reproducible

# More details on the courses

### Best practices for programming for scientists (2 x 2h presentation)

{% include figure.liquid loading="eager" path="assets/img/ide.png" width=400 class="img-fluid rounded z-depth-1 mx-auto d-block" zoomable=true %}
<div class="caption">
    Part of this class includes showing how to use a software IDE to efficiently debug your code
</div>

- Coding pitfalls (classic bugs you need to know about)
- Programming paradigms (writing maintainable code)
- Using Integrated Development Environments (IDEs) for fast and efficient programming
- Debugging code
- Version control with `git`
- Testing your code
- Leveraging AI tools

See also my blog posts on [writing proper code]({% post_url 2024-07-20-good-code-1-proper-naming-in-scientific-code %}) and [programming paradigms]({% post_url 2024-10-27-good-code-2-solid-principles %}).

<br/>

### Version control with `git` for scientists (integrated presentation and workshop, 4h total)

{% include figure.liquid loading="eager" path="assets/img/git_training.jpg" width=400 class="img-fluid rounded z-depth-1 mx-auto d-block" zoomable=true %}
<div class="caption">
    Illustration of the difference between the two `git` concepts, `merge` and `rebase`.
</div>

- What are the benefits of version control and why should all code be in version control?
- What is `git`, what is `Github`?
- Setting everything up
- Understanding the benefits of version control and how to make use of it
- How to properly use `git`
  - commits
  - branches
  - merging
  - checking what has changed
  
You can find the content of the workshop here: <a href="https://github.com/k-gregor/git-workshop">https://github.com/k-gregor/git-workshop</a>
  
<br/>

### Monitoring and optimizing resource usage of scientific code (~3h presentation, potentially with workshop)

{% include figure.liquid loading="eager" path="assets/img/blogpostimgs/mprof.png" width=400 class="img-fluid rounded z-depth-1 mx-auto d-block" zoomable=true %}
<div class="caption">
    Profiling a python script to find memory leaks
</div>

- Understanding the memory architecture of computers
- How to monitor total usage of computer programs
- Professional profiling tools
- A brief introduction to data structures and runtime analysis (*O-notation*)
- Programming memory-efficiently
	- chunking
	- data types
	- lazy loading
	- in-place operations

See also my blog post on this topic: [memory aspects in scientific code]({% post_url 2024-11-17-memory-aspects-in-scientific-coding %})

<br/>

### Using the command line and bash scripting to speed up scientific workflows (integrated presentation and workshop, 4h total)

{% include figure.liquid loading="eager" path="assets/img/terminal.png" width=400 class="img-fluid rounded z-depth-1 mx-auto d-block" zoomable=true %}
<div class="caption">
    The command line is a powerful tool to find and manipulate data swiftly, and to automate workflows. This example shows a simple way to figure out how many grid cells of all sub-processes of a modeling exercise have successfully simulated until the year 2010.
</div>

This covers topics that are helpful both when working locally or on a supercomputer.

- Navigating through files and directories
- Finding data quickly
- Superfast data manipulation in the command line
- Writing scripts to automate workflows
- Monitoring resource usage of data analyses

<br/>

### Introduction to Continuous Integration and Continuous Deployment (~1h presentation)

{% include figure.liquid loading="eager" path="assets/img/lpjci.png" width=400 class="img-fluid rounded z-depth-1 mx-auto d-block" zoomable=true %}
<div class="caption">
    CI offers numerous tools to automatically ensure the quality of your code and to foster collaboration.
</div>

- Collaborating
- Automated documentation
- Code linting
- Automated testing
- Issue tracking
- Versioning

<br/>

### Making quantitative research reproducible (Presentation 2h, potentially with workshop)


{% include figure.liquid loading="eager" path="assets/img/snakemake_dag.png" width=400 class="img-fluid rounded z-depth-1 mx-auto d-block" zoomable=true %}
<div class="caption">
    Tools like `snakemake` can help make your workflows 100% reproducible. This figure shows the automated pipeline from my ISIMIP project, including downloading, cropping, merging, and mapping data, and combining it to model input files.
</div>


- Making scientific workflows reproducible with `snakemake` (Python) or `targets` (R)
- Dockerize your code to make it run anywhere
