
# DBT Streamlit Monitoring

This project is for DBT Cloud users who want to be able to share information on how
their jobs are performing, but without granting Admin access to DBT Cloud directly.

The app builds a nice interactive dashboard using Streamlit, which allows people to see
which jobs are completing successfully (or failing) and lets you see the specific steps
where a job is falling over.

You'll need to add some secrets specific to your environment, but other than that you
should be up and running right out of the box.




## Features

- Supports multiple projects on the same DBT Account
- RAG Status of jobs
- Show failed steps, with links to the specific file in your repo
- Get a view of recent job runs to see if there's an ongoing issue with your job


## Installation

Install and run locally with pipenv

```bash
  pipenv install
  pipenv run app
```

For Mac users watchdog is included as a dev dependency, so you can include watchdog with

```bash
  pipenv install -d
```
## Configuration

Unless you're a massive fan of Cazoo (I mean, who isn't!) you might want to swap out the
logo for your own.

### secrets.toml
The app in its current form assumes the presence of a few things which will be custom to
each DBT account, and so we put these in secrets.toml inside of .streamlit.

Running streamlit locally will use these secrets (accessible both as environment variables
and from streamlit.secrets) and if you decide to deploy onto Streamlit for Teams then you
can use the same format to add your secrets directly into the web interface.

ACCOUNT_ID - your DBT account id

API_TOKEN - your DBT API key (for very obvious reasons we don't commit this to version control).

dashboard_user / dashboard_pass - username/password for the authorisation (please see
below for why this is probably not a good thing to use)

PROJECT_MAPPING - This is mapping that links specific DBT project ids to a plain English name
for displaying in the app. The project mapping is used to drive the select boxes that allow you
pick specifc projects to drill down to (if you have multiple projects of course).


BQ_BASE_URL / REDSHIFT_BASE_URL - Now, it's possible that this might be a bit Cazoo specific, but I
hope it finds some use elsewhere. This comes from two main pieces;
* When we have job failures, our analysts asked for a link directly to the repo for that file.
* We currently have two main repos for DBT, one for all Big Query jobs and one for Redshift

These URLs are the 'base' url for our repos that link to the repo, branch, and the folder within.
So as an example;

https://github.com/MyCompany/MyRepo/tree/main/my_folder/

This is a repo hosted on GitHub, the repo is called MyRepo, has 'main' as the primary repo branch
and within the repo all the dbt work is in a folder called my_folder.

In open sourcing this we took a decision that most interested people are likely to be using Big Query
or Redshift, and so this will be useful functionality.  But if you're using something else let us know, or
even better raise a PR to add functionality into the app!
