# LASR Cards - Software Development Risks

## Table of Contents

- [1. Software Solution](#1-software-solution)
  - [1.1 Overly complex solution](#11-overly-complex-solution)
  - [1.2 Unsuitable software structure](#12-unsuitable-software-structure)
  - [1.3 Inadequate data handling](#13-inadequate-data-handling)
  - [1.4 Problematic concepts & technologies](#14-problematic-concepts--technologies)
- [2. Competence and Experience](#2-competence-and-experience)
  - [2.1 Missing / isolated technical knowledge](#21-missing--isolated-technical-knowledge)
  - [2.2 Isolated / distributed domain knowledge](#22-isolated--distributed-domain-knowledge)
  - [2.3 Missing or worthless tool support](#23-missing-or-worthless-tool-support)
  - [2.4 Too little room for experiments / learning](#24-too-little-room-for-experiments--learning)
- [3. Goals and Expectations](#3-goals-and-expectations)
  - [3.1 Very high goals or expectations](#31-very-high-goals-or-expectations)
  - [3.2 Restrictive org. constraints (time / budget)](#32-restrictive-org.-constraints-time--budget)
  - [3.3 No direct contact with customers or users](#33-no-direct-contact-with-customers-or-users)
  - [3.4 Vague / implicit / unclear objectives](#34-vague--implicit--unclear-objectives)
- [4. External Systems and Platforms](#4-external-systems-and-platforms)
  - [4.1 Negative side effects](#41-negative-side-effects)
  - [4.2 Unstable / unsuitable external systems](#42-unstable--unsuitable-external-systems)
  - [4.3 Platform problems](#43-platform-problems)
  - [4.4 Vendor-lock-in or support problems](#44-vendor-lock-in-or-support-problems)
- [5. Legacy Systems and Technical Debt](#5-legacy-systems-and-technical-debt)
  - [5.1 Obstructive legacy solutions](#51-obstructive-legacy-solutions)
  - [5.2 Innovation deficit / technical debt](#52-innovation-deficit--technical-debt)
  - [5.3 Poorly understood solution](#53-poorly-understood-solution)
  - [5.4 Fragile or interwoven system parts](#54-fragile-or-interwoven-system-parts)
- [6. Organization and Processes](#6-organization-and-processes)
  - [6.1 Organizational boundaries](#61-organizational-boundaries)
  - [6.2 Non-practical decision-makers](#62-non-practical-decision-makers)
  - [6.3 Obstructive or swollen processes](#63-obstructive-or-swollen-processes)
  - [6.4 Restrictive standards or constraints](#64-restrictive-standards-or-constraints)
- [7. Operations and Deployment](#7-operations-and-deployment)
  - [7.1 Low maturity in deployment / release](#71-low-maturity-in-deployment--release)
  - [7.2 Blocking CI/CD processes](#72-blocking-cicd-processes)
  - [7.3 Insufficient insight / overview in operations](#73-insufficient-insight--overview-in-operations)
  - [7.4 Lack of operational concepts](#74-lack-of-operational-concepts)
- [8. Soft Factors](#8-soft-factors)
  - [8.1 Disagreements on the solution design](#81-disagreements-on-the-solution-design)
  - [8.2 Poorly defined roles and responsibilities](#82-poorly-defined-roles-and-responsibilities)
  - [8.3 Incompatible or inappropriate culture](#83-incompatible-or-inappropriate-culture)
  - [8.4 Communication barriers](#84-communication-barriers)

---

## 1. Software Solution

### 1.1 Overly complex solution

Is the domain particularly complex? Are there any rash or quick solutions? Are abstractions used inadequately? Complexity jeopardizes understandability and in turn maintainability, correctness, ...

---

### 1.2 Unsuitable software structure

Is the software structured according to the domain? Does it take other technical and organizatorial influences (Conway...) into account? If not, maintainability, reliability etc. could suffer.

---

### 1.3 Inadequate data handling

Is the storage, transport and mapping of data conceptually and technically appropriate? Is data is in the right places, in the right format - in time and legally compliant?

---

### 1.4 Problematic concepts & technologies

Do the implemented patterns and concepts support the product's goals? Are they applied consistently? Are the technologies and frameworks used both suitable and well established?

---

## 2. Competence and Experience

### 2.1 Missing / isolated technical knowledge

Is technical knowledge lacking or unevenly spread? Is there a lack of practical experience? This can lead to complex, inconsistent or downright incorrect solutions.

---

### 2.2 Isolated / distributed domain knowledge

Is the domain knowledge too shallow to find good abstractions and apply concepts correctly? Is communication with business experts hard, complicated, indirect or slowing?

---

### 2.3 Missing or worthless tool support

Do tools interfere with the modification of software, its operation or with team communication? Are other tools or processes required to reach high dev maturity? Are repetitive tasks done manually?

---

### 2.4 Too little room for experiments / learning

Do the teams feel overly pressured to deliver features? Is failure during test, deployment or release too expensive? Is there enough interaction and experimentation to learn and stay innovative?

---

## 3. Goals and Expectations

### 3.1 Very high goals or expectations

Are quality attributes (e.g. performance) too ambitious? Do individual objectives stand in the way of overall product quality? Are there problematic tradeoffs between goals or with constraints?

---

### 3.2 Restrictive org. constraints (time / budget)

Are deadlines or budgets weighing heavily on the team? Is there any room for experiments and innovation? Is a quick solution always more important than documentation, technical debt, ...?

---

### 3.3 No direct contact with customers or users

Is product development lacking direct costumer feedback? Are customer needs, stakeholder interests or usage patterns of the solution unclear, ambiguous or based on hearsay?

---

### 3.4 Vague / implicit / unclear objectives

Are strategic goals or quality criteria poorly understood? Are objectives too vague to support the discussion of architectural alternatives? Can stakeholders understand tradeoffs?

---

## 4. External Systems and Platforms

### 4.1 Negative side effects

Could other projects, external systems or organizations potentially disrupt development? Do competing activities negatively influence the budget, sourcing or choice of technology?

---

### 4.2 Unstable / unsuitable external systems

Do third-party systems interfere with development or operation? Are external APIs, interfaces, message formats or transport technologies volatile? Are SLAs incompatible?

---

### 4.3 Platform problems

Do pipelines, platforms, test- or ops-environments hinder development or operations in any way? Are there any problematic restrictions on usage, compatibility or cost?

---

### 4.4 Vendor-lock-in or support problems

Are there any dependencies on suppliers whose objectives are very different? Are there potential problems with discontinuations, support, license models, costs, ...?

---

## 5. Legacy Systems and Technical Debt

### 5.1 Obstructive legacy solutions

Are existing systems or components hindering development? Are they unstable, fragile, tightly coupeled, difficult to integrate or understand? Reliability or maintainability are often affected.

---

### 5.2 Innovation deficit / technical debt

Is the risk of change hindering technical and conceptional improvements? Do postponed improvements threaten quality objectives such as maintainability, reliability or security?

---

### 5.3 Poorly understood solution

Is knowledge or documentation for parts of the system missing? Are specialists or experts scarce? Are parts of the solution difficult to understand or have they "grown historically"?

---

### 5.4 Fragile or interwoven system parts

Does the system suffer from weak structuring, tangled code, bad tests or low coverage? Is the system prone to side effects? Are quality characteristics tested?

---

## 6. Organization and Processes

### 6.1 Organizational boundaries

Do skill and knowledge disparities threaten the consistency of the system? Are organizational boundaries, such as departments, limiting or slowing the work on complex solution parts?

---

### 6.2 Non-practical decision-makers

Are important technical decisions often made by people outside the development team or in central roles? Does this threaten their applicability, their acceptance or team motivation?

---

### 6.3 Obstructive or swollen processes

Do current processes hinder decision making or collaboration? Are regulations and politics often a focal point? Are painful dicussions across teams often necessary?

---

### 6.4 Restrictive standards or constraints

Are architecture decisions (often) complicated by standards, budget or time constraints? Are there restrictive legal aspects, e.g. relating to data handling or internationalization?

---

## 7. Operations and Deployment

### 7.1 Low maturity in deployment / release

Are deployments/releases expensive or risky? Are CI/CD processes poorly automated or error-prone? Do development teams lack knowledge of platforms and pipelines?

---

### 7.2 Blocking CI/CD processes

Are teams slowed down or interrupted by deployment processes? Is the release complicated by strict deployment sequences or "freeze times"? Do backlog items often depend on other teams?

---

### 7.3 Insufficient insight / overview in operations

Do development teams lack insight into the production environment? Are they unprepared for errors or failures? Are reaction times slow or is it hard to find responsible people to fix a problem?

---

### 7.4 Lack of operational concepts

Are monitoring, capacity planning, backup, disaster recovery, (security) alerting, ... backed by sound concepts? Are these concepts well supported by tools and widely known or adopted?

---

## 8. Soft Factors

### 8.1 Disagreements on the solution design

Are central design decisions (e.g. the use of technologies, frameworks, integration strategies or data storage approaches) often derailed by conflicts, deadlocks or immovable personal opinions?

---

### 8.2 Poorly defined roles and responsibilities

Are roles clearly defined? Do teams respond quickly or do problems often "cascade" through different roles? Are deadlocks or "ping-pong effects" common when decisions are made?

---

### 8.3 Incompatible or inappropriate culture

Are cultural and architectural styles compatible (e.g. independent services -> autonomous teams)? Does freedom in development and design lead to accountable decision-making in teams?

---

### 8.4 Communication barriers

Is cross-team dialog tough or hindered by barriers? Is it rare to get (fast) feedback for software changes or technical experiments? Is the knowledge distribution somewhat imbalanced?

---

