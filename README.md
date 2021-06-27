---
title: "AnSir-homework backend"
disqus: hackmd
---

# Project Title

![downloads](https://img.shields.io/github/downloads/atom/atom/total.svg)
![build](https://img.shields.io/appveyor/ci/:user/:repo.svg)
![mind chat](https://img.shields.io/discord/:serverId.svg)
![mind chat](https://gitmind.com/app/flowchart/0f32674809)

## Overview

[TOC]

## Requirements

Python (3.8.5)

## Learn about

mindmap:https://gitmind.com/app/doc/b3c2649404
mindchart(user):https://gitmind.com/app/flowchart/0f32674809
postman example:https://documenter.getpostman.com/view/13057025/TzecDRFz
functional note:

## Quick start

### Installation

1. Clone the repository
2. create a virtual environment using virtualenv venv
3. Activate the virtual environment by running source venv/bin/activate
4. Install the dependencies

```
pip install -r requirement.txt
```

5. make .env
6. Migrate existing db tables by running python

```
python manage.py makemigrations
python manage.py migrate
```

7. Run the django development server using python

```
manage.py runserver
```

## API Endpoint

athentication

- /auth/register/
- /auth/login/
- /auth/request-reset-email/
- /auth/password-reset/NjY/ao86jf-463b3871cf255a85a4ef41c7424b7893/?redirect_url=

cases

- /cases/
- /cases/<id>

## User flows

```sequence
register
verify email
login -> get Bearer token

case CRUD
point CRUD
```

## api testing

```
//swagger ui
url: {{baseUrl}}/swagger

// postman
in folder postman_examples
```

## Project Timeline

```mermaid
gantt
    title A Gantt Diagram

    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    anther task      : 24d
```

> Read more about mermaid here: http://mermaid-js.github.io/mermaid/

## Appendix and FAQ

:::info
**Find this document incomplete?** Leave a comment!
:::

###### tags: `Templates` `Documentation`
