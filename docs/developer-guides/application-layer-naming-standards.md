# Application Naming Standard

## Purpose

This document outlines a standard naming convention for the application.

To design a standard naming system for **features**, **commands**, **queries**, **events**, **handlers**, **validators**, **responses**, we want a scheme that is:

-   **Consistent** (predictable and navigable)
-   **Descriptive** (clear about intent and behavior)
-   **Scalable** (can grow with your system)
-   **Aligned to CQRS/Event-Driven patterns** (where applicable)

## Naming Convention Overview

### Feature Name (Namespace)

Each feature groups related behaviors.

-   **Format:** `FeatureName` (PascalCase, Noun or NounPhrase)
-   **Examples:**
    -   `Blog`
    -   `UserAccount`
    -   `Analysis`
    -   `SubscriptionPlan`

### Command Names (Imperative)

Used for write-side actions that **cause a state change**.

-   **Format:** `{Verb}{Object}` (PascalCase, imperative mood)
-   **Namespace:** `Features.{FeatureName}.{ActionName}`
-   **Examples:**
    -   `CreatePost`
    -   `UpdateProfile`
    -   `RunAnalysis`
    -   `CancelSubscription`

### Query Names (Descriptive)

Used for read-side actions that **return data**.

-   **Format:** `Get{Entity}` or `List{Entities}` or `Search{Entity}`
-   **Namespace:** `Features.{FeatureName}.{ActionName}`
-   **Examples:**
    -   `GetPostById`
    -   `ListPublishedPosts`
    -   `SearchUsers`
    -   `GetSleepReportByDogId`

### Event Names (Past Tense)

Events describe something that **has already happened**.

-   **Format:** `{Entity}{PastTenseVerb}` or `{Verb}{Entity}Occurred`
-   **Namespace:** `Features.{FeatureName}.{ActionName}`
-   **Examples:**
    -   `PostPublished`
    -   `UserLoggedIn`
    -   `AnalysisCompleted`
    -   `SubscriptionCancelled`

### Handler Names

Handlers execute the logic for a command, query, or event.

-   **Format:** `{ActionName}Handler` (PascalCase)
-   **Namespace:** `Features.{FeatureName}.{ActionName}`
-   **Examples:**
    -   `CreateUserCommandHandler`
    -   `GetUserQueryHandler`
    -   `UserLoggedInEventHandler`
    -   `AnalyzeDataCommandHandler`

### Validator Names

Validators enforce business rules and input validation for commands and queries.

-   **Format:** `{ActionName}Validator` (PascalCase)
-   **Namespace:** `Features.{FeatureName}.{ActionName}`
-   **Examples:**
    -   `CreateUserCommandValidator`
    -   `GetUserQueryValidator`
    -   `AnalyzeDataCommandValidator`

### Response Names

Response types represent the result of a command or query.

-   **Format:** `{ActionName}Response` (PascalCase)
-   **Namespace:** `Features.{FeatureName}.{ActionName}`
-   **Examples:**
    -   `CreateUserResponse`
    -   `GetUserResponse`
    -   `AnalyzeDataResponse`

## Directory / Code Structure

```plaintext
/Application
  /Features
    /{FeatureName}
      /{ActionName}
        {CommandName/QueryName/EventName}.cs
        {HandlerName}.cs
        {ValidatorName}.cs
        {ResponseName}.cs
```

## General Rules

-   Use PascalCase for all type names.
-   Keep names concise but descriptive.
-   The suffix (`Command`, `Query`, `Event`, `Handler`, `Validator`, `Response`) must always be present and in the correct order.
-   For complex actions, use `ActionEntity` (e.g., `GenerateSegmentProfilesCommandHandler`).

This standard ensures that all core application types are easily discoverable and their purpose is clear from their name.
