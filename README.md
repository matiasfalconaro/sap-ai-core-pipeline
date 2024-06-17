# AI core

This Folder contains sample notebooks and workflow templates that can enable the user to have a quick hands-on with SAP AI Core

DISCLAIMER: The tutorials and notebooks contain sample codes and are only for enablement and not for Production usage.

The sample notebooks and the workflow templates demonstrate as to how to productise a simple Business ML use case to SAP AI Core. The whole idea is to have a Plug and Play approach, however there are certain Prerequisites to be met before you start using the notebooks and workflow templates

## Content Structure

```
.
├── <tutorial-name>/                Descriptive name
│   ├── utils/                      Utilities
│   ├── <notebook-name>.ipynb       Main Jupyter Notebook
│   └── credentials.yaml            Credentials related to the tutorial
│
.
.
.
│
├── credentials.yaml.template       Template for credentials storage
└── README.md
```

## Getting credentials via BTP platform

Go to SAP BTP Cockpit
Select a space
Select the services option on the left menu
Find the default_aicore service

## Getting credentials via terminal

- `cf login`
- `cf target -o <organization> -s default`
- `cf services | grep aicore` # To find which aicore services are running. In our case we should only find dev-pgo-aicore
- `cf service-keys <service>` # To list service keys associated with the service
- `cf service-key <service> <service-key-name>`

## Credentials template

Copy `credentials.yaml.template` and rename it as `credentials.yaml`.
Replace the placeholders with the credentials Json file values.

## SAP AI Launchpad app

[Baitcon development - SAP AI Launchpad](https://baitcondevelopment.ai-launchpad.prod.us-east-1.aws.apps.ml.hana.ondemand.com/)

## Tutorials

|Turorial name|URL|Repoitory|Comments|
|-------------|---|---------|--------|
|Set Up Tools to Connect With and Operate SAP AI Core|[ai-core-setup](https://developers.sap.com/tutorials/ai-core-setup.html)|[01](https://github.com/SAP-samples/ai-core-samples/tree/main/02_ai_core/tutorials/01_create_your_first_machine_learning_project_using_sap_ai_core/01_01_set_up_tools_to_connect_with_and_operate_sap_ai_core)||
|Quick Start for Your First AI Project Using SAP AI Core|[ai-core-helloworld](https://developers.sap.com/tutorials/ai-core-helloworld.html)|[02]https://github.com/SAP-samples/ai-core-samples/tree/main/02_ai_core/tutorials/01_create_your_first_machine_learning_project_using_sap_ai_core/01_02_quick_start_for_your_first_ai_project_using_ai_core)||