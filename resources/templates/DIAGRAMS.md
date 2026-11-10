# Diagram conventions

Use Mermaid for diagrams that should remain editable in Markdown.

## Generic data flow
```mermaid
flowchart TD
    A[Input] --> B[Validation]
    B --> C[Preprocessing]
    C --> D[Model or service]
    D --> E[Postprocessing]
    E --> F[Output]
```

## Request/response sequence
```mermaid
sequenceDiagram
    participant U as User
    participant API as Backend API
    participant M as Model
    U->>API: Send request
    API->>API: Validate and prepare input
    API->>M: Invoke model
    M-->>API: Model output
    API-->>U: Structured response
```

Label external services, data stores, trust boundaries and asynchronous steps explicitly. Avoid implying a component exists in a project until it is verified.
