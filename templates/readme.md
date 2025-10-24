# {{ header.name }}

{% for name, contact_info in header.contact.items() %}
{{- name }}: {{ contact_info }}
{% endfor %}
{{ header.location }}

{{ header.tagline }}


## Technical Skills
{% for category, technologies in body['Technical Skills'].items() %}
#### {{ category }}
{{ technologies | join(", ") }}
{% endfor %}

## Core Competencies
{% for line in body['Core Competencies'] %}
{{ line | join(", ") }}
{% endfor %}

## Professional Experience
{% for job in body['Professional Experience'] %}
#### {{ job.employer }}

Title: {{ job.title }}
Tenure: {{ job.tenure.start }} – {{ job.tenure.end }}
Location: {{ job.location }}{%
  if 'short description' in job %}

{{ job['short description'] }}
{% endif %}
{% for point in job['main points'] %}
- {{ point }}
{% endfor %}
{%- endfor %}

## Education
{% for degree in body['Education'] %}
#### {{ degree.degree }}
Institution: {{ degree.institution }}{%
  if 'date' in degree %}
Date: {{ degree.date }}{% endif %}
{% endfor %}

## Certifications 
{% for cert in body['Certifications'] %}
#### {{ cert.certification }}
ID: {{ cert.id }}
Date: {{ cert.date }}
{% endfor %}
