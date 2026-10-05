"""Portfolio content summarized from the owner's September 2026 résumé."""
SKILLS = [
    ('ERP & backend', ['Odoo', 'Python', 'Node.js', 'REST APIs', 'PostgreSQL', 'Microsoft SQL Server']),
    ('AI & automation', ['LangChain', 'LangGraph', 'LLMs', 'RAG', 'AI agents', 'Vector databases', 'OCR', 'Pydantic']),
    ('Engineering & leadership', ['JavaScript', 'Linux', 'DevOps', 'Code review', 'Agile delivery', 'Team mentoring']),
]
EXPERIENCE = [
    {'period': 'Aug 2025 — Present', 'role': 'Odoo Technical Lead / AI Engineer', 'company': '365 INFOTECH', 'location': 'Bangkok, Thailand', 'summary': 'Leading scalable Odoo implementations and enterprise AI solutions, from architecture and custom modules to intelligent agents, integrations, and production delivery.', 'tags': ['Technical leadership', 'Enterprise AI', 'Odoo']},
    {'period': 'Oct 2022 — Jul 2025', 'role': 'Senior Odoo Developer', 'company': 'VCT Consulting (Thailand) Co., Ltd', 'location': 'Bangkok, Thailand', 'summary': 'Delivered custom ERP modules, business workflows, and third-party integrations. Guided technical decisions, optimized performance, and mentored junior developers.', 'tags': ['ERP development', 'System integration', 'Mentoring']},
    {'period': 'Sep 2018 — Sep 2022', 'role': 'Odoo Developer', 'company': 'Seventh Computing Co., Ltd', 'location': 'Yangon, Myanmar', 'summary': 'Built and customized Odoo across CRM, HRMS, manufacturing, sales, and accounting, with Python, XML, JavaScript, and PostgreSQL.', 'tags': ['Odoo customization', 'Full-cycle delivery']},
    {'period': 'May 2018 — Aug 2018', 'role': 'Trainee Web Developer', 'company': 'Myanmar IT Consulting Co., Ltd', 'location': 'Yangon, Myanmar', 'summary': 'Developed web interfaces with PHP, HTML, CSS, and JavaScript, supporting testing, debugging, and server management.', 'tags': ['Web development', 'PHP']},
]
PROJECTS = [
    {'title': 'Enterprise AI Platform', 'category': 'ai', 'label': 'AI & AUTOMATION', 'type': 'ai', 'role': 'Architecture & development lead', 'description': 'An intelligent layer connecting Odoo and legacy business systems with knowledge retrieval, AI agents, and document intelligence.', 'tags': ['LangGraph', 'RAG', 'Odoo', 'LLMs'], 'details': 'Designed stateful multi-agent workflows with tool execution, conversation memory, human approval, and checkpoints. Integrated secure ERP APIs, Microsoft SQL Server, OCR extraction, semantic search, and natural-language analytics with access controls and audit trails.'},
    {'title': 'Poysian ERP Implementation', 'category': 'erp', 'label': 'MANUFACTURING & ERP', 'type': 'erp', 'role': 'Lead Odoo Developer · 10-person team', 'description': 'Connected sales, purchasing, inventory, accounting, and manufacturing in one integrated Odoo implementation.', 'tags': ['Odoo', 'Manufacturing', 'Accounting'], 'details': 'Led a team of 10 members implementing Sales, Purchase, Inventory, Accounting, and Manufacturing modules to support operational efficiency and integrated business processes.'},
    {'title': 'Live Plaza Myanmar', 'category': 'commerce', 'label': 'E-COMMERCE & ERP', 'type': 'commerce', 'role': 'Development lead · 6-person team', 'description': 'An e-commerce implementation bringing online sales, inventory, purchasing, and accounting together.', 'tags': ['E-commerce', 'Odoo', 'Inventory'], 'details': 'Led six staff members in the Odoo development of the Live Plaza Myanmar E-commerce Project, implementing E-commerce, Sales, Purchase, Inventory, and Accounting modules.'},
    {'title': 'TOA Paint (Thailand)', 'category': 'erp', 'label': 'MANUFACTURING & ERP', 'type': 'erp', 'role': 'Senior Odoo Developer', 'description': 'Integrated core manufacturing and commercial operations with tailored Odoo business workflows.', 'tags': ['Odoo', 'Manufacturing', 'Integration'], 'details': 'Led an Odoo implementation covering Sales, Purchase, Inventory, Accounting, and Manufacturing, managing development and supporting process optimization.'},
    {'title': 'The Cool Group', 'category': 'erp', 'label': 'BUSINESS OPERATIONS', 'type': 'erp', 'role': 'Lead Odoo Developer · 5-person team', 'description': 'Aligned CRM and commercial operations through a connected enterprise resource planning system.', 'tags': ['CRM', 'Sales', 'Accounting'], 'details': 'Managed a team of five members implementing CRM, Sales, Purchase, Inventory, and Accounting modules to improve business workflows and system performance.'},
    {'title': 'TATO Contacts', 'category': 'commerce', 'label': 'E-COMMERCE & ERP', 'type': 'commerce', 'role': 'Lead Odoo Developer · 6-person team', 'description': 'Connected e-commerce and back-office workflows across orders, stock, purchasing, and finance.', 'tags': ['E-commerce', 'Inventory', 'Accounting'], 'details': 'Led a team of six members implementing E-commerce, Sales, Purchase, Inventory, and Accounting modules.'},
]

# Remaining projects listed in the résumé's Accomplishments section.
_RESUME_PROJECTS = [
    ('Yoma Fleet', 'Odoo Developer', 5, 'CRM, Fleet, Sales, Accounting'),
    ('ABC Mall', 'Odoo Developer', 3, 'CRM, Sales, Inventory'),
    ('Myanmar Kaido', 'Odoo Developer', 4, 'CRM, Sales, Purchase, Accounting'),
    ('Myanmar Awba', 'Odoo Developer', 5, 'CRM, Sales, Accounting, Inventory'),
    ('Orchid Pharmacy', 'Odoo Developer', 3, 'Sales, Inventory, Accounting'),
    ('Autonova Service & Collision Repair Center', 'Odoo Developer', 4, 'Maintenance, Accounting'),
    ('Sagoseeds Microfinance', 'Odoo Developer', 5, 'CRM, Accounting, Website'),
    ('Great Wall International', 'Odoo Developer', 3, 'Accounting, Purchasing, Inventory'),
    ('Honda Myanmar', 'Odoo Developer', 4, 'Sales, Purchase, Inventory'),
    ('Alpha Power Engineering', 'Odoo Developer', 5, 'Purchasing, Inventory, HR'),
    ('El Dorado Bake House', 'Odoo Developer', 3, 'POS, Sales, Inventory, Purchase'),
    ('Shwe Taung Myanmar Engineering & Construction', 'Odoo Developer', 6, 'Sales, Accounting, Manufacturing, Inventory, Purchase'),
    ('IEM Company', 'Odoo Developer', 4, 'Sales, Purchase, Inventory, Accounting'),
    ('Sun Mobile IT & Electronic', 'Odoo Developer', 5, 'Sales, POS, E-commerce, Inventory'),
    ('Htun Myat Aung Property Development', 'Odoo Developer', 3, 'Sales, Accounting'),
    ('Joker Biscuits & Cookies', 'Odoo Developer', 6, 'Sales, Purchase, Expense, Inventory, Accounting, Manufacturing'),
    ('Myanmar Distribution Group (MDG)', 'Odoo Developer', 4, 'Sales, Purchase, Inventory, E-commerce'),
    ('Fairdeal FMCG Distribution', 'Odoo Developer', 5, 'Sales, Purchase, Inventory, HR'),
    ('Skyway Myanmar Apparel', 'Odoo Developer', 3, 'Sales, Inventory, HR'),
    ('Myport Limited', 'Odoo Developer', 4, 'Inventory, Maintenance'),
    ('Medicare Myanmar', 'Odoo Developer', 3, 'HR'),
    ('Padetha Distribution', 'Odoo Developer', 5, 'Sales, Purchase, Inventory, Accounting'),
    ('TOKYO Pipe', 'Odoo Developer', 4, 'Sales, Purchase, Accounting, Inventory'),
    ('MOMO International Trading', 'Odoo Developer', 5, 'Sales, Purchase, Inventory, Accounting'),
    ('RENE Mattuas Myanmar', 'Odoo Developer', 3, 'POS, Sales, Inventory, Accounting'),
    ('Sysnet System & Distribution', 'Odoo Developer', 3, 'CRM, Sales'),
    ('City Property Development', 'Odoo Developer', 4, 'Sales, Purchase, Inventory, Accounting'),
    ('Saw Bwar Gyi Gone E-commerce', 'Senior Odoo Developer', 5, 'E-commerce, Sales, Purchase, Inventory'),
    ('TG Phone System', 'Senior Odoo Developer', 5, 'Sales, POS, Inventory, Accounting, E-commerce'),
    ('Djing Retail Ayutthaya', 'Senior Odoo Developer', 3, 'Sales, Inventory, Accounting'),
    ('City Fresh Food', 'Senior Odoo Developer', 4, 'Sales, Purchase, Inventory, Accounting'),
    ('GVS Recycling', 'Senior Developer', 5, 'Manufacturing, Sales, Purchase, Inventory, Accounting'),
    ('JAGTAR Thai Silk', 'Senior Odoo Developer', 3, 'Sales, Accounting, Inventory'),
    ('Indochina Development Partner Sole Lao', 'Senior Developer', 6, 'Manufacturing, Inventory, Purchase, Sales, Accounting, Expense, Employee, Time Off'),
    ('The FireFocus', 'Lead Odoo Developer', 4, 'CRM, Sales, Purchase, Inventory, Accounting'),
]
for title, role, team_size, module_text in _RESUME_PROJECTS:
    modules = module_text.split(', ')
    category = 'commerce' if 'E-commerce' in modules else 'erp'
    lead = role == 'Lead Odoo Developer'
    PROJECTS.append({
        'title': title,
        'category': category,
        'type': category,
        'label': 'E-COMMERCE & ERP' if category == 'commerce' else 'ODOO ERP IMPLEMENTATION',
        'role': f'{role} · {team_size}-person team',
        'description': f'Odoo implementation covering {module_text}.',
        'tags': modules,
        'details': f'{"Led" if lead else "Collaborated with"} a team of {team_size} members as {role}, implementing {module_text} modules.'
    })

EDUCATION = [
    ('2013 — 2018', 'Bachelor of Computer Science', 'University of Computer Studies, Monywa · Myanmar'),
    ('2019 — 2020', 'International Diploma in Project Management', 'OTHM, UK · Myanmar Figure Institute'),
    ('2019 — 2020', 'International Diploma in Strategic Business Management', 'OTHM, UK · Myanmar Figure Institute'),
]
