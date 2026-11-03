from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
R=Path(__file__).resolve().parents[1];out=R/'assets/resumes';out.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('CV','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'));pdfmetrics.registerFont(TTFont('CV-Bold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'));pdfmetrics.registerFontFamily('CV',normal='CV',bold='CV-Bold')
b=ParagraphStyle('body',fontName='CV',fontSize=9,leading=14,spaceAfter=9,textColor=HexColor('#20252a'))
h=ParagraphStyle('heading',parent=b,fontName='CV-Bold',fontSize=11,spaceBefore=13,spaceAfter=8)
t=ParagraphStyle('title',parent=b,fontName='CV-Bold',fontSize=24,leading=30,spaceAfter=8)
roles={
'BA':('Business Analyst','Information Technology graduate with project experience discussing business needs with a company owner, translating needs into workflows and developing a public website and CMS. Interested in requirements analysis, process improvement and stakeholder communication.', [('Yuyenpensuk Website & CMS','Discussed website needs with the company owner, designed content-management workflows and developed the public catalogue and CMS. Prepared source-derived requirements, business rules and acceptance scenarios.'),('AI PPE Inspection - BA Assessment','Prepared a proposed inspection workflow, stakeholder questions, functional and non-functional requirements, acceptance criteria and UAT planning. This is an assessment proposal, not a deployed AI system.'),('Agricultural Prices Pipeline','Worked on source integration, validation and presentation of public prices from DIT, NABC and Talaadthai. Dashboard comparisons retain consistent units, measurement types and dates.')], 'Requirements Gathering | Functional Requirements | Business Rules | Workflow Design | Acceptance Criteria | UAT Planning | Data Flow | SQL | Technical Documentation | GitHub'),
'SA':('System Analyst','Information Technology graduate with project experience in system workflows, data structures and web development. Interested in translating business requirements into clear application boundaries, data flows and implementation specifications.', [('Yuyenpensuk Website & CMS','Developed a Node.js / Express / EJS catalogue and CMS with JSON file storage and image-upload handling. Reviewed public/admin architecture and prepared source-derived data-flow, logical-data-model and endpoint documentation.'),('Agricultural Prices Pipeline','Worked on an Airflow pipeline with data validation and PostgreSQL UPSERT, plus a Streamlit dashboard reading the database. Defined conditions for comparable price groups.'),('Animal Adoption - Schema Design','Designed relational entities for animals, adopters and adoption requests, with primary and foreign keys. The repository contains schema-level work; an operational backend is not claimed.')], 'System Analysis | Requirements Traceability | DFD | Logical Data Modeling | Relational Schema | SQL | Node.js | Express | JavaScript | REST Concepts | Docker | GitHub'),
'Data_Analyst':('Data Analyst','Information Technology graduate with project experience in data collection, validation, SQL and dashboard workflows. Interested in preparing reliable datasets and explaining analysis with clear source, unit and time context.', [('Agricultural Prices Pipeline','Integrated public prices from DIT, NABC and Talaadthai using Python, Airflow and PostgreSQL. Applied validation and deduplication, with a Streamlit dashboard for filtering and visualization.'),('GoldSense - Thai Gold Price Tracking','Project uses an HTTP data source and SQLite for price observations and a dashboard. Repository evidence records a price publication; no trained forecast or evaluated model is claimed.'),('MotoInsight - Data Preparation','Prepared Python source for CheckRaka HTML parsing, CSV export, duplicate removal, missing-value handling and descriptive summaries. A completed dashboard or evaluated dataset is not claimed.')], 'SQL | PostgreSQL | SQLite | Python | Pandas | Data Cleaning | Data Validation | ETL | Airflow | Streamlit | Data Visualization | GitHub')}
for key,(role,profile,projects,skills) in roles.items():
 story=[]
 def p(s,style=b):story.append(Paragraph(s,style))
 p('PANUPONG INTASAN',t);p(role+' | Available November 2026')
 p('<link href="mailto:intasan25@gmail.com">intasan25@gmail.com</link> | <link href="https://github.com/intasan">github.com/intasan</link><br/><link href="https://intasan.github.io/portfolio/">intasan.github.io/portfolio/</link>')
 story.append(HRFlowable(width='100%',thickness=1,color=HexColor('#424651')))
 p('PROFILE',h);p(profile)
 p('EDUCATION',h);p("<b>Kasetsart University, Kamphaeng Saen Campus</b><br/>Bachelor's Degree in Information Technology | 2023-2026")
 p('SELECTED PROJECT EXPERIENCE',h)
 for title,desc in projects:p('<b>'+title+'</b><br/>'+desc)
 p('RELEVANT SKILLS',h);p(skills)
 p('LANGUAGE & WORKING APPROACH',h);p('English: KU-EXITE 79/100, CEFR B2 (2026). Uses ChatGPT Work to assist research, documentation and coding, with source review and validation before presenting results.')
 SimpleDocTemplate(str(out/f'Panupong_Intasan_{key}.pdf'),pagesize=A4,leftMargin=44,rightMargin=44,topMargin=38,bottomMargin=38,title=f'Panupong Intasan - {role}',author='Panupong Intasan').build(story)
 print(key)
