# N8B Summary of forecast literature

This is a summary review of the information contained in other documents in this section. We briefly describe (and point to some useful high-level resources) main forecasts and key points related to later stages of the project.

For a much more detailed review and resource collection of population projections please see the DetailedNotes.md document in this folder.

## Key forecasts

We consider the following forecasts to be relevant to the project.

- United Nations Population Division: Population Prospects
- Witgenstein Centre population projection
- Global Burden of Disease Study (AKA: the Lancet model)
- Earth4All model

## Description of key forecasts

The following are high level summaries of the key forecasts, aimed at summarising the key points, impacts and relevance to the N8B analysis, for a concise review of how the first three (all bar the Earth4All model) fit together in the context of population modelling see [the Earth4All "People and Planet" report](https://earth4all.life/wp-content/uploads/2023/04/E4A_People-and-Planet_Report.pdf) (section "2. Overview of main demographic approaches")

### United Nations Population Division: Population Prospects

#### Overview

Primary forecast under consideration.

The UNPD model does not consider external drivers of population growth (i.e. an apolitical/policy-decision independent strategy), predicting the future population on the basis of:
- "Ageing" cohorts
- Accounting for births and deaths (and modelling future from historical patterns)
- Modelling migration

This is the foundational basis for the majority of population forecasts, and is well established in the field.

#### Data

The UNPD projections use a vast collection of data sources [documented here](https://population.un.org/wpp/Publications/Files/WPP2022_Data_Sources.pdf). These sources are collected together to build a "best achievable" picture of the population across the World, and these include analyst-applied adjustments to refine the estimates according to known effects (e.g. [age heaping](https://en.wikipedia.org/wiki/Whipple's_index)). This gives a "best guess" to populations, fertility, mortality and migration globally, and this dataset is relied upon in other works (not least some of the other projections we consider).

#### Uncertainty

Recent additions to the UNPD projection are probabilistic models for fertility and mortality.

[This brief guide to uncertainty](https://www.un.org/en/development/desa/population/publications/pdf/popfacts/PopFacts_2019-6.pdf) provides an overview and some visualisation of the uncertainty in the projections, stating that uncertainty comes from three sources: fertility, mortality and migration (with the former being the biggest driver of uncertainty)[^1]

[^2]: Strictly there is an uncertainty on the data, which doesn't seem to be pulled into the prediction, I haven't found this addressed anywhere so seems reasonable to take this as assumed negligible.

#### Scenarios

The UNPD projections model the following scenarios:

- Several different fertility assumptions:
  - Low, medium, high
  - Constant-fertility
  - Instant-replacement (TODO: confirm interpretation as tot births==tot deaths per year)
- An addition to the instant replacement scenario which also assumes zero-migration[^2]
- Finally a momentum scenario with alternative mortality assumptions to the above is incorporated

[^2]: Technical note: Need to validate but this seems essentially the same approach as taking the largest eigenvalue of the Leslie matrix - insofar as it's looking at asymptotics of a constant model

#### Fertility and mortality transitions

The UNPD WPP projection fertility and mortality models depend on the assumption of a fertility and mortality transition (a shift from a higher level of birth and death rate to a lower - also known as [an epidemiological transition](https://en.wikipedia.org/wiki/Epidemiological_transition)). These transitions have been observed, studied and statistically fit to a particular pattern.

UNPD models have account for these transitions using a model of their general structure. A more recent development was to refine curve fitting (parameter estimation)  in such a way that would also provide [the uncertainty mentioned above](#Uncertainty) ([Bayesian model described in this technical paper](https://arxiv.org/pdf/1405.4708.pdf)).

### Witgenstein Centre population projection
### Lancet model (TODO: check proper title)
### Earth4All model
