# LASR-Karten - Risiken der Softwareentwicklung

## Table of Contents

- [1. Softwareloesung](#1-softwareloesung)
  - [1.1 Zu hohe Komplexität der Lösung](#11-zu-hohe-komplexität-der-lösung)
  - [1.2 Unpassende Lösungs-Strukturierung](#12-unpassende-lösungs-strukturierung)
  - [1.3 Inadäquates Daten-Handling](#13-inadäquates-daten-handling)
  - [1.4 Problematische Konzepte & Technologien](#14-problematische-konzepte--technologien)
- [2. Kompetenz und Erfahrung](#2-kompetenz-und-erfahrung)
  - [2.1 Fehlendes / Isoliertes technisches Wissen](#21-fehlendes--isoliertes-technisches-wissen)
  - [2.2 Isoliertes / verteiltes Domänenwissen](#22-isoliertes--verteiltes-domänenwissen)
  - [2.3 Falsche / fehlende Tool-Unterstützung](#23-falsche--fehlende-tool-unterstützung)
  - [2.4 Zu wenig Freiraum für Experimente / Lernen](#24-zu-wenig-freiraum-für-experimente--lernen)
- [3. Zielsetzungen und Erwartungen](#3-zielsetzungen-und-erwartungen)
  - [3.1 Zu hohe Ziele oder Erwartungen](#31-zu-hohe-ziele-oder-erwartungen)
  - [3.2 Einengender Projektrahmen (Zeit / Budget)](#32-einengender-projektrahmen-zeit--budget)
  - [3.3 Fehlender Kunden- / Nutzerkontakt](#33-fehlender-kunden---nutzerkontakt)
  - [3.4 Vage / implizite / unklare Zielsetzungen](#34-vage--implizite--unklare-zielsetzungen)
- [4. Fremdsysteme und Plattformen](#4-fremdsysteme-und-plattformen)
  - [4.1 Negative Seiteneffekte](#41-negative-seiteneffekte)
  - [4.2 Instabile / unpassende Fremdsysteme](#42-instabile--unpassende-fremdsysteme)
  - [4.3 Probleme mit der technischen Plattform](#43-probleme-mit-der-technischen-plattform)
  - [4.4 Vendor-Lock-In oder Support-Probleme](#44-vendor-lock-in-oder-support-probleme)
- [5. Altsysteme und Altlasten](#5-altsysteme-und-altlasten)
  - [5.1 Behindernde Legacy-Lösungen](#51-behindernde-legacy-lösungen)
  - [5.2 Innovationsstau / Technische Schulden](#52-innovationsstau--technische-schulden)
  - [5.3 Fehlendes Lösungsverständnis](#53-fehlendes-lösungsverständnis)
  - [5.4 Brüchige, schwer änderbare Systemteile](#54-brüchige-schwer-änderbare-systemteile)
- [6. Organisation und Prozesse](#6-organisation-und-prozesse)
  - [6.1 Zu hoher Verteilungsgrad](#61-zu-hoher-verteilungsgrad)
  - [6.2 Praxisferne Entscheidungsträger](#62-praxisferne-entscheidungsträger)
  - [6.3 Behindernde oder geschwollene Prozesse](#63-behindernde-oder-geschwollene-prozesse)
  - [6.4 Einengende Standards oder Randbedingungen](#64-einengende-standards-oder-randbedingungen)
- [7. Betrieb und Deployment](#7-betrieb-und-deployment)
  - [7.1 Wenig Reife bei Deployment- / Release](#71-wenig-reife-bei-deployment---release)
  - [7.2 Blockierende CI/CD Prozesse](#72-blockierende-cicd-prozesse)
  - [7.3 Zu wenig Einblick / Überblick im Betrieb](#73-zu-wenig-einblick--überblick-im-betrieb)
  - [7.4 Fehlende Betriebskonzepte](#74-fehlende-betriebskonzepte)
- [8. Weiche Faktoren](#8-weiche-faktoren)
  - [8.1 Uneinigkeit bei der Lösungsgestaltung](#81-uneinigkeit-bei-der-lösungsgestaltung)
  - [8.2 Unklare Rollen und Verantwortlichkeiten](#82-unklare-rollen-und-verantwortlichkeiten)
  - [8.3 Unpassende oder inkompatible Kultur](#83-unpassende-oder-inkompatible-kultur)
  - [8.4 Kommunikationsbarrieren](#84-kommunikationsbarrieren)

---

## 1. Softwareloesung

### 1.1 Zu hohe Komplexität der Lösung

Hat die Domäne eine sehr hohe Komplexität? Gibt es unüberlegte, schnelle Lösungen oder fehlende Abstraktionen? Komplexität gefährdet den Überblick bzw. Wartbarkeit, Korrektheit, Sicherheit, ...

---

### 1.2 Unpassende Lösungs-Strukturierung

Folgt die Softwarestruktur der Domäne? Sind andere technische oder organisatorische Einflüsse (Conway...) gut aufgegriffen? Falls nicht könnte Wartbarkeit, Zuverlässigkeit etc. leiden

---

### 1.3 Inadäquates Daten-Handling

Ist die Ablage, der Transport und das Mapping von Daten konzeptionell und technisch passend gelöst? Sind Daten ausreichend schnell und rechtssicher, im richtigen Format an den richtigen Stellen?

---

### 1.4 Problematische Konzepte & Technologien

Passen die eingesetzten Muster und Konzepte zu den Zielen? Sind sie konsistent angewendet? Sind die verwendeten Technologien und Frameworks passend und etabliert?

---

## 2. Kompetenz und Erfahrung

### 2.1 Fehlendes / Isoliertes technisches Wissen

Ist technisches Wissen nicht, oder nur punktuell vorhanden? ist es unpassend oder fehlt die praktische Erfahrung? Das kann zu komplexen, inkonsistenten oder schlicht fehlerhaften Lösungen führen.

---

### 2.2 Isoliertes / verteiltes Domänenwissen

Ist das Domänenwissen tief genug, um die richtigen Abstraktionen zu finden und Konzepte richtig abzubilden? Ist die Kommunikation mit Fachexperten einfach und auf Augenhöhe?

---

### 2.3 Falsche / fehlende Tool-Unterstützung

Behindern Werkzeuge bei Änderungen, Betrieb oder Kommunikation? Fehlen wichtige Tools oder Prozesse für hohe Development Maturity (CI/CD)? Sind repetitive Aufgaben manuell abgebildet?

---

### 2.4 Zu wenig Freiraum für Experimente / Lernen

Ist der "Feature-Druck" auf Teams hoch? Ist Scheitern in Test, Deployment und Release eher teuer? Gibt es genügend Austausch und Experimente um innovations- und lernfähig zu bleiben?

---

## 3. Zielsetzungen und Erwartungen

### 3.1 Zu hohe Ziele oder Erwartungen

Sind Qualitätsziele (z.B. Performanz) zu ambitioniert? Stehen hohe Einzelziele guter Gesamtqualität im Weg? Werden Randbedingungen verletzt oder unnötige technische Risiken eingegangen?

---

### 3.2 Einengender Projektrahmen (Zeit / Budget)

Wie hoch ist der terminliche oder budgetäre Druck? Bleibt genügend Freiraum für Expiremente und Innovation? Sind Themen wie Dokumentation oder technische Schulden gut bespielt?

---

### 3.3 Fehlender Kunden- / Nutzerkontakt

Kommt der funktionale und qualitative Fokus von "außen"? Sind die Bedürfnisse von Kunden, die Interessen von Stakeholdern und Verwendungsmuster von Benutzern klar und häufig validiert?

---

### 3.4 Vage / implizite / unklare Zielsetzungen

Sie die strategischen und qualitativen Ziele klar? Sind sie spezifisch genug, um Architekturalternativen gegeneinander abzuwägen? Können Kompromisse mit Stakeholdern besprochen werden?

---

## 4. Fremdsysteme und Plattformen

### 4.1 Negative Seiteneffekte

Gibt es potentiell Behinderungen durch Nachbarprojekte oder fremde Organisationseinheiten? Gibt es konkurrierende Tätigkeiten, die Budget, Verfügbarkeiten oder Technologiewahl beeinflussen?

---

### 4.2 Instabile / unpassende Fremdsysteme

Behindern ("interne") Fremdsysteme bei Entwicklung oder Betrieb? Ändern sich APIs, Schnittstellen, Nachrichtenformate oder Transporttechnologien potentiell / häufig? Sind SLAs inkompatibel?

---

### 4.3 Probleme mit der technischen Plattform

Machen Betriebsumgebung und Deployment-Plattform die Entwicklung / den Betrieb einfacher? Sind Komplexität, Kosten, Benutzungs- oder Kompatibilitätseinschränkungen problematisch?

---

### 4.4 Vendor-Lock-In oder Support-Probleme

Gibt es Abhängigkeiten von Lieferanten, deren Ziele oder Einsatzzwecke abweichen? Stehen Abkündigungen im Raum? Gibt es potentielle Probleme bei Support, Lizenzmodellen, Kosten, ...?

---

## 5. Altsysteme und Altlasten

### 5.1 Behindernde Legacy-Lösungen

Behindern Altsysteme oder -systemteile? Sind sie schwer einzubinden, instabil oder schwer verständlich? Sind sie stark verwoben oder brüchig? Zuverlässigkeit oder Wartbarkeit sind häufig betroffen.

---

### 5.2 Innovationsstau / Technische Schulden

Bleiben technische oder konzeptionelle Möglichkeiten ungenutzt, weil Änderungen zu risikoreich sind? Sind Qualitätsziele wie Wartbarkeit oder Sicherheit durch aufgeschobene Verbesserungen bedroht?

---

### 5.3 Fehlendes Lösungsverständnis

Fehlen Wissen, Ansprechpartner und/oder Dokumentation für Teile des Systems? Sitzen Ansprechpartner an Bottlenecks? Sind zentrale Lösungen tw. wenig nachvollziehbar oder "historisch gewachsen"?

---

### 5.4 Brüchige, schwer änderbare Systemteile

Sind Teile der Lösung schlecht dokumentiert, verwoben oder nicht mit (guten) Tests abgedeckt? Treten bei Änderungen unerwartete Seiteneffekte auf? Fehlen Tests zu Qualitätseigenschaften?

---

## 6. Organisation und Prozesse

### 6.1 Zu hoher Verteilungsgrad

Ist die Konsistenz des Systems durch abweichende Wissensstände bedroht? Behindern natürliche Organisationsgrenzen wie Abteilungen oder Standorte die Arbeit an komplexen Lösungsteilen?

---

### 6.2 Praxisferne Entscheidungsträger

Liegen wichtige technische Entscheidungen eher bei entwicklungsfernen oder zentralen Rollen? Ist die Anwendbarkeit von Ergebnissen, deren Akzeptanz oder generell die Dynamik dadurch bedroht?

---

### 6.3 Behindernde oder geschwollene Prozesse

Behindern die gelebten Prozesse bei Zusammenarbeit oder Entscheidungen? Stehen Regeln / Politik oft im Zentrum? Müssen viele Themen übergreifend diskutiert werden? Ist das zäh?

---

### 6.4 Einengende Standards oder Randbedingungen

Werden Architekturentscheidungen (oft) durch Standards, Budget- oder Zeitbeschränkungen erschwert? Gibt es einschneidende rechtliche Aspekte rund um Daten oder Internationalisierung?

---

## 7. Betrieb und Deployment

### 7.1 Wenig Reife bei Deployment- / Release

Sind Deployments / Releases teuer oder risikoreich? Sind die CI/CD Prozesse wenig automatisiert oder fehleranfällig? Haben Entwicklungsteams Wissen im Bereich Plattformen und Pipelines?

---

### 7.2 Blockierende CI/CD Prozesse

Ist der Arbeitsrhytmus von Teams durch Deployment-Prozesse behindert? Gibt es wichtige Deployment-Reihenfolgen oder "Freeze-Zeiten" beim Release? Hängen Backlog-Items oft von anderen Teams ab?

---

### 7.3 Zu wenig Einblick / Überblick im Betrieb

Ist die Betriebsumgebung eine Blackbox für Entwicklungsteams? Treten Fehler / Kosten oft überraschend auf? Wird bei Problemen langsam reagiert oder ist es schwer die richtigen Personen zu finden?

---

### 7.4 Fehlende Betriebskonzepte

Gibt es gute Konzepte für Capacity Planning, Backup, Disaster Recovery, (Security-)Alerting, ...? Sind diese Konzepte gut durch Tools unterstützt und breit bekannt bzw. anwendbar?

---

## 8. Weiche Faktoren

### 8.1 Uneinigkeit bei der Lösungsgestaltung

Gibt es bei zentralen Entscheidungen (wie eingesetzten Technologien oder Frameworks, dem Integrationsansatz oder der Datenablage) Konflikte oder verhärtete Meinungsfronten?

---

### 8.2 Unklare Rollen und Verantwortlichkeiten

Sind Rollen inkl. deren Grenzen definiert? Wird bei Problemen schnell reagiert oder "kaskadieren" Probleme häufig über Rollen? Kommt es bei Entscheidungen zu Blockaden oder "Ping-Pong-Effekten"?

---

### 8.3 Unpassende oder inkompatible Kultur

Sind Kultur und Architekturstil kompatibel (z.b. Unabhängige Services -> freier agierende Teams)? Hat "Offenheit" der Prozesse auch reale Verantwortungsübernahme in den Teams zur Folge?

---

### 8.4 Kommunikationsbarrieren

Gibt es Kommunikationsbarrieren oder fehlende teamübergreifende Austauschformate? Ist (technisches) Feedback zur Lösung eher selten oder verzögert? Ist die Wissensverteilung eher ungleich?

---

