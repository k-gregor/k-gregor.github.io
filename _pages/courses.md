---
layout: page
title: courses
nav: true
permalink: /courses/
---

<style>
  .courses-hero {
    text-align: center;
    padding: 2.5rem 1.5rem;
    margin-bottom: 2.5rem;
    border-radius: 1rem;
    background: linear-gradient(135deg, color-mix(in srgb, var(--global-theme-color) 14%, transparent), color-mix(in srgb, var(--global-theme-color) 3%, transparent));
    border: 1px solid color-mix(in srgb, var(--global-theme-color) 25%, transparent);
  }
  .courses-hero .kicker {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--global-theme-color);
  }
  .courses-hero h2 {
    font-size: 2.1rem;
    font-weight: 700;
    margin: 0.5rem 0 1rem;
  }
  .courses-hero p {
    max-width: 640px;
    margin: 0 auto 1.25rem;
    font-size: 1.1rem;
  }
  .btn-cta {
    display: inline-block;
    padding: 0.6rem 1.4rem;
    border-radius: 2rem;
    background: var(--global-theme-color);
    color: var(--global-hover-text-color) !important;
    font-weight: 600;
    text-decoration: none !important;
    transition: transform 0.15s, box-shadow 0.15s;
  }
  .btn-cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px color-mix(in srgb, var(--global-theme-color) 35%, transparent);
  }

  .logo-strip {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 2.5rem;
    margin: 1rem 0 3rem;
  }
  .logo-strip figure { margin: 0; }
  .logo-strip img {
    height: 70px;
    width: auto;
    filter: grayscale(100%);
    opacity: 0.75;
    transition: filter 0.2s, opacity 0.2s;
  }
  .logo-strip img:hover { filter: none; opacity: 1; }
  .section-label {
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.8rem;
    color: var(--global-text-color-light);
  }

  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0 3rem;
  }
  .feature {
    padding: 1.25rem;
    border-radius: 0.75rem;
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
  }
  .feature i {
    font-size: 1.5rem;
    color: var(--global-theme-color);
    margin-bottom: 0.5rem;
  }
  .feature h4 { font-size: 1.05rem; font-weight: 600; margin: 0.25rem 0 0.4rem; }
  .feature p { margin: 0; font-size: 0.95rem; color: var(--global-text-color-light); }

  .course-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
    margin: 1rem 0 3rem;
  }
  .course-chips a, .course-chips span {
    padding: 0.35rem 0.9rem;
    border-radius: 2rem;
    border: 1px solid var(--global-theme-color);
    color: var(--global-theme-color);
    font-size: 0.9rem;
    text-decoration: none !important;
    transition: background 0.15s, color 0.15s;
  }
  .course-chips a:hover {
    background: var(--global-theme-color);
    color: var(--global-hover-text-color);
  }

  .course-card {
    border-radius: 1rem;
    overflow: hidden;
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    margin-bottom: 2rem;
    scroll-margin-top: 80px;
    transition: box-shadow 0.2s, transform 0.2s;
  }
  .course-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.1);
  }
  .course-media {
    background: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1.25rem;
    min-height: 180px;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .course-media figure { margin: 0; }
  .course-media img {
    max-height: 240px;
    max-width: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
  }
  .course-body { padding: 1.5rem 1.75rem; }
  .course-body h3 { font-size: 1.4rem; font-weight: 700; margin: 0 0 0.5rem; }
  .course-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-bottom: 1rem;
  }
  .badge-pill-soft {
    font-size: 0.8rem;
    padding: 0.2rem 0.7rem;
    border-radius: 2rem;
    background: color-mix(in srgb, var(--global-theme-color) 14%, transparent);
    color: var(--global-theme-color);
    font-weight: 600;
  }
  .course-caption {
    font-style: italic;
    font-size: 0.92rem;
    color: var(--global-text-color-light);
    margin-bottom: 1rem;
  }
  .course-body ul { padding-left: 1.2rem; margin-bottom: 0.75rem; }
  .course-body li { margin-bottom: 0.2rem; }
  .course-body li::marker { color: var(--global-theme-color); }
  .course-links {
    margin-top: 1rem;
    padding-top: 0.75rem;
    border-top: 1px dashed var(--global-divider-color);
    font-size: 0.95rem;
  }

  .extra-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
    margin-bottom: 3rem;
  }
  .extra-grid .feature h4 { margin-top: 0; }

  .cta-box {
    text-align: center;
    padding: 2.25rem 1.5rem;
    border-radius: 1rem;
    background: var(--global-theme-color);
    color: var(--global-hover-text-color);
    margin: 1rem 0 2rem;
  }
  .cta-box h2 { color: inherit; font-weight: 700; margin-top: 0; }
  .cta-box p { max-width: 560px; margin: 0 auto 1.25rem; }
  .cta-box .btn-cta {
    background: var(--global-hover-text-color);
    color: var(--global-theme-color) !important;
  }

  @media (max-width: 576px) {
    .courses-hero h2 { font-size: 1.6rem; }
    .course-body { padding: 1.25rem; }
    .logo-strip { gap: 1.5rem; }
    .logo-strip img { height: 50px; }
  }
</style>

<div class="courses-hero">
  <div class="kicker">Courses &amp; workshops for research groups</div>
  <h2>Learning coding topics in the age of AI? <br/>Yes!</h2>
  <p>
    Even with agentic coding, it's crucial to know the key fundamentals of clean and robust software engineering.
    I distilled the most important aspects of software engineering for scientists: from <code>git</code> version control,
    over code-testing, common bugs and pitfalls, to reproducible workflow pipelines.
  </p>
  <a class="btn-cta" href="mailto:konstantin.gregor@posteo.de"><i class="fa-solid fa-envelope"></i>&nbsp; Get in touch</a>
</div>

<div class="section-label">I have taught courses at</div>
<div class="logo-strip">
{% include figure.liquid loading="eager" path="assets/img/lund.svg" height=70 width="auto" alt="Lund University" %}
{% include figure.liquid loading="eager" path="assets/img/berkeley.png" height=70 width="auto" alt="University of California, Berkeley" %}
{% include figure.liquid loading="eager" path="assets/img/egu.png" height=70 width="auto" alt="European Geosciences Union" %}
{% include figure.liquid loading="eager" path="assets/img/tum.png" height=70 width="auto" alt="Technical University of Munich" %}
</div>

<div class="feature-grid">
  <div class="feature">
    <i class="fa-solid fa-laptop-house"></i>
    <h4>In-person or online</h4>
    <p>Courses usually consist of a presentation part and a hands-on workshop part.</p>
  </div>
  <div class="feature">
    <i class="fa-solid fa-sliders"></i>
    <h4>Fully customizable</h4>
    <p>Topics are adapted to your group's needs, as not all aspects may be relevant for everyone.</p>
  </div>
  <div class="feature">
    <i class="fa-solid fa-circle-question"></i>
    <h4>Interactive</h4>
    <p>Even the presentation-heavy courses include quizzes and small tasks.</p>
  </div>
  <div class="feature">
    <i class="fa-solid fa-robot"></i>
    <h4>AI-ready</h4>
    <p>I show how to use AI tools effectively in technical tasks, where universities are still far behind what could be done.</p>
  </div>
</div>

From my experience, the **Best practices for programming for scientists** and **Fundamentals of data science** courses are highly useful for most research groups. They are mostly presentations, but still interactive, with quizzes and small tasks. The other courses contain both presentation and hands-on workshop parts.

<div class="section-label" style="margin-top: 2.5rem;">Courses at a glance</div>
<div class="course-chips">
  <a href="#best-practices">Best practices for programming</a>
  <a href="#git">Version control with <code>git</code></a>
  <a href="#ai">Programming successfully with AI</a>
  <a href="#resources">Monitoring &amp; optimizing resource usage</a>
  <a href="#ci">Continuous Integration &amp; Deployment</a>
  <a href="#reproducible">Reproducible research</a>
  <a href="#more">Fundamentals of data science</a>
  <a href="#more">Fundamentals of programming in Python</a>
</div>

<!-- ============ Best practices ============ -->
<div class="course-card" id="best-practices">
  <div class="course-media">
    {% include figure.liquid loading="eager" path="assets/img/ide.png" zoomable=true alt="Debugging in an IDE" %}
  </div>
  <div class="course-body">
    <h3>Best practices for programming for scientists</h3>
    <div class="course-meta">
      <span class="badge-pill-soft"><i class="fa-regular fa-clock"></i> 2 × 2h</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-person-chalkboard"></i> Presentation</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-star"></i> Most popular</span>
    </div>
    <div class="course-caption">Part of this class includes showing how to use a software IDE to efficiently debug your code.</div>
    <ul>
      <li>Coding pitfalls (classic bugs you need to know about)</li>
      <li>Programming paradigms (writing maintainable code)</li>
      <li>Using Integrated Development Environments (IDEs) for fast and efficient programming</li>
      <li>Debugging code</li>
      <li>Version control with <code>git</code></li>
      <li>Testing your code</li>
      <li>Leveraging AI tools</li>
    </ul>
    <div class="course-links">
      <i class="fa-solid fa-book-open"></i> Related blog posts:
      <a href="{% post_url 2024-07-20-good-code-1-proper-naming-in-scientific-code %}">writing proper code</a> ·
      <a href="{% post_url 2024-10-27-good-code-2-solid-principles %}">programming paradigms</a>
    </div>
  </div>
</div>

<!-- ============ git ============ -->
<div class="course-card" id="git">
  <div class="course-media">
    {% include figure.liquid loading="eager" path="assets/img/git_commits.png" zoomable=true alt="A git commit history" %}
  </div>
  <div class="course-body">
    <h3>Version control with <code>git</code> for scientists</h3>
    <div class="course-meta">
      <span class="badge-pill-soft"><i class="fa-regular fa-clock"></i> 4h total</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-person-chalkboard"></i> Presentation</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-laptop-code"></i> Hands-on workshop</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-calendar-check"></i> Again at EGU 2027</span>
    </div>
    <ul>
      <li>What are the benefits of version control and why should all code be in version control?</li>
      <li>What is <code>git</code>, what is <code>GitHub</code>?</li>
      <li>Setting everything up</li>
      <li>Understanding the benefits of version control and how to make use of it</li>
      <li>How to properly use <code>git</code>: commits, branches, merging, checking what has changed</li>
    </ul>
    <div class="course-links">
      <i class="fa-brands fa-github"></i> Workshop material:
      <a href="https://github.com/k-gregor/git-workshop">github.com/k-gregor/git-workshop</a>
      <br/>
      <i class="fa-solid fa-earth-europe"></i> Given as a short course at
      <a href="https://meetingorganizer.copernicus.org/EGU26/EGU26-7637.html">EGU 2026</a>,
      and it will be offered again at EGU 2027!
    </div>
  </div>
</div>

<!-- ============ AI ============ -->
<div class="course-card" id="ai">
  <div class="course-media">
    {% include figure.liquid loading="eager" path="assets/img/chatgpt.png" zoomable=true alt="Chatting with an AI assistant" %}
  </div>
  <div class="course-body">
    <h3>Beyond "vibe-coding": programming successfully with AI</h3>
    <div class="course-meta">
      <span class="badge-pill-soft"><i class="fa-regular fa-clock"></i> ~3h</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-person-chalkboard"></i> Presentation</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-laptop-code"></i> Optional workshop</span>
    </div>
    <div class="course-caption">New AI tools are here to help with coding. But they should be used wisely!</div>
    <p>
      AI is here to stay and you'd have a competitive disadvantage if you didn't use it. Anyone can ask ChatGPT to write them some code.
      But do you just "vibe-code" or use the tools at hand efficiently? In this workshop, we will look into:
    </p>
    <ul>
      <li>How to efficiently program with AI tools</li>
      <li>How to make sure AI-generated or AI-influenced code is correct</li>
      <li>How can teachers detect AI-generated code?</li>
    </ul>
  </div>
</div>

<!-- ============ Resources ============ -->
<div class="course-card" id="resources">
  <div class="course-media">
    {% include figure.liquid loading="eager" path="assets/img/blogpostimgs/mprof.png" zoomable=true alt="Memory profile of a Python script" %}
  </div>
  <div class="course-body">
    <h3>Monitoring and optimizing resource usage of scientific code</h3>
    <div class="course-meta">
      <span class="badge-pill-soft"><i class="fa-regular fa-clock"></i> ~3h</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-person-chalkboard"></i> Presentation</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-laptop-code"></i> Optional workshop</span>
    </div>
    <div class="course-caption">Profiling a Python script to find memory leaks.</div>
    <ul>
      <li>Understanding the memory architecture of computers</li>
      <li>How to monitor total usage of computer programs</li>
      <li>Professional profiling tools</li>
      <li>A brief introduction to data structures and runtime analysis (<em>O-notation</em>)</li>
      <li>Programming memory-efficiently: chunking, data types, lazy loading, in-place operations</li>
    </ul>
    <div class="course-links">
      <i class="fa-solid fa-book-open"></i> Related blog post:
      <a href="{% post_url 2024-11-17-memory-aspects-in-scientific-coding %}">memory aspects in scientific code</a>
    </div>
  </div>
</div>

<!-- ============ CI ============ -->
<div class="course-card" id="ci">
  <div class="course-media">
    {% include figure.liquid loading="eager" path="assets/img/lpjci.png" zoomable=true alt="A CI pipeline" %}
  </div>
  <div class="course-body">
    <h3>Introduction to Continuous Integration and Continuous Deployment</h3>
    <div class="course-meta">
      <span class="badge-pill-soft"><i class="fa-regular fa-clock"></i> ~1h</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-person-chalkboard"></i> Presentation</span>
    </div>
    <div class="course-caption">CI offers numerous tools to automatically ensure the quality of your code and to foster collaboration.</div>
    <ul>
      <li>Collaborating</li>
      <li>Automated documentation</li>
      <li>Code linting</li>
      <li>Automated testing</li>
      <li>Issue tracking</li>
      <li>Versioning</li>
    </ul>
  </div>
</div>

<!-- ============ Reproducible ============ -->
<div class="course-card" id="reproducible">
  <div class="course-media">
    {% include figure.liquid loading="eager" path="assets/img/snakemake_dag.png" zoomable=true alt="A snakemake workflow graph" %}
  </div>
  <div class="course-body">
    <h3>Making quantitative research reproducible</h3>
    <div class="course-meta">
      <span class="badge-pill-soft"><i class="fa-regular fa-clock"></i> 2h</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-person-chalkboard"></i> Presentation</span>
      <span class="badge-pill-soft"><i class="fa-solid fa-laptop-code"></i> Optional workshop</span>
    </div>
    <div class="course-caption">
      Tools like <code>snakemake</code> can help make your workflows 100% reproducible. This figure shows the automated pipeline from my ISIMIP project,
      including downloading, cropping, merging, and mapping data, and combining it to model input files.
    </div>
    <ul>
      <li>Making scientific workflows reproducible with <code>snakemake</code> (Python) or <code>targets</code> (R)</li>
      <li>Dockerize your code to make it run anywhere</li>
    </ul>
  </div>
</div>

<!-- ============ More ============ -->
<div class="section-label" id="more" style="margin-top: 2.5rem; scroll-margin-top: 80px;">Also available</div>
<div class="extra-grid" style="margin-top: 1rem;">
  <div class="feature">
    <i class="fa-solid fa-chart-line"></i>
    <h4>Fundamentals of data science</h4>
    <p>Highly useful for most research groups. Mostly a presentation, but interactive with quizzes and small tasks.</p>
  </div>
  <div class="feature">
    <i class="fa-brands fa-python"></i>
    <h4>Fundamentals of programming in Python</h4>
    <p>An introduction to programming in Python.</p>
  </div>
</div>

<div class="cta-box">
  <h2>Interested in a course for your group?</h2>
  <p>Do not hesitate to reach out and we can discuss potential courses tailored to your group's needs!</p>
  <a class="btn-cta" href="mailto:konstantin.gregor@posteo.de"><i class="fa-solid fa-envelope"></i>&nbsp; Write me an e-mail</a>
</div>
