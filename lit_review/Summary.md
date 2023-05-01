# N8B Summary of forecast literature

<!-- toc -->

- [Key forecasts](#key-forecasts)
- [Description of key forecasts](#description-of-key-forecasts)
  * [United Nations Population Division: Population Prospects](#united-nations-population-division-population-prospects)
    + [Overview](#overview)
    + [Data](#data)
    + [Uncertainty](#uncertainty)
    + [Scenarios](#scenarios)
    + [Fertility and mortality transitions](#fertility-and-mortality-transitions)
  * [Witgenstein Centre population projection](#witgenstein-centre-population-projection)
    + [Overview](#overview-1)
    + [Data](#data-1)
    + [Uncertainty](#uncertainty-1)
    + [Scenarios](#scenarios-1)
    + [Other](#other)
  * [Lancet model (TODO: check proper title)](#lancet-model-todo-check-proper-title)
    + [Overview](#overview-2)
    + [Data](#data-2)
    + [Uncertainty](#uncertainty-2)
    + [Scenarios](#scenarios-2)
    + [Other](#other-1)
  * [Earth4All model](#earth4all-model)
    + [Overview](#overview-3)
    + [Data](#data-3)
    + [Uncertainty](#uncertainty-3)
    + [Scenarios](#scenarios-3)
    + [Other](#other-2)

<!-- tocstop -->

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

[^1]: Strictly there is an uncertainty on the data, which doesn't seem to be pulled into the prediction, I haven't found this addressed anywhere so seems reasonable to take this as assumed negligible.

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

#### Key criticisms

The main criticism of the UNPD WPP projections is that they are pure time-series models, not accounting for anything but models of fertility and mortality (see [Lancet model paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2820%2930677-2/fulltext) and the [Earth4All People and Planet report](https://earth4all.life/wp-content/uploads/2023/04/E4A_People-and-Planet_Report.pdf)).

### Witgenstein Centre population projection

#### Overview
#### Data
#### Uncertainty
#### Scenarios
#### Other


### Global Burden of Disease study (aka: Lancet model)

#### Overview

The Global Burden of Disease study is detailed [in this Lancet paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2820%2930677-2/fulltext) (hence the pseudonym).

As the name suggests this study is focused on understanding the impacts of 

#### Data
#### Uncertainty
#### Scenarios
#### Other


### Earth4All model

#### Overview

The dynamics of the Earth4All are structurally different to the above, for the main reason that while population is one of things it projects it is critically a projection of multiple interacting factors (this is true to an extent in the second Lancet and Wittgenstein models but structurally this is a different class of model).

In essence there is a model for population, and a model for (e.g.) GDP, Climate,... but these then have an impact on each other over each timestep, so one models the "entire" interacting system. The image below is a useful schematic for understanding how some of the key factors interact.

![High level schematic](https://github.com/Niallfealty/n8b_un_foundation/blob/main/lit_review/images/Earth4All_major_sectors_diagram.png)

In some sense one can look at this as a collection of models for different processes all of which depend to a degree on one another - this makes interpretation somewhat difficult in a mathematical perspective due to interdependency (it may be less clear how the dynamics of one system depend on another) and fully grasping the assumptions of the model[^3]

[^3]: There is mentioned that due to the nuance and complexity of the model there is not yet a single comprehensive model description, and indeed the modelling is described over a nuber of detailed reports, some of which we cite in this document [some further key publications are available here](https://earth4all.life/publications/).

[The stated purpose](https://earth4all.life/) for the Earth4All group is to understand what is needed from transformational economics on a finitely-resourced planet to sustain its population. Thus there is a direct interest in understanding policy impacts on population (and other modelled metrics) - so one may think of this as the opposite end of the spectrum to the UNPD WPP: i.e. a "political" model.

#### Data

[In the methodology paper](https://eartharxiv.org/repository/view/5111/) data is referenced from numerous sources (though there doesn't seem to be sourcing for the model data so far). One of these is "UN Population statistics" which could plausibly be the UN population data the UNPD WPP is based on. More generally, while there are sources for data used in the technical paper on methodology, and [some summaries of model parameters available](https://stockholmuniversity.app.box.com/s/uh7fjh52pvh7yx1mqfwqcyxdcvegrodf/folder/170483416144) here, there doesn't as yet appear to be a definitive set of data sources as yet.

#### Uncertainty

Similarly there are some model uncertainties provided, but no specific methodology. It seems reasonable to suppose (from some descriptions of the software and prior experience of the territory along with similar software) that this is a Monte-Carlo simulation and outputs a predictive distribution - which can then be used to generate an uncertainty. This is merely a supposition for the time being however.

#### Scenarios

They model two scenarios:

- Too Little Too Late (TLTL)
- Giant Leap (GL)

The difference between these two scenarios is stated as the following:
```
Poverty Turnaround:
Accelerate GDP growth in countries with less than 15 k$/p/y using modern technology –debt
cancellation, new development models, more industrial policy and infant industry protection
Inequality Turnaround:
Take from the few rich and give to the many poor – higher taxes on owners used to improve the
wellbeing of the working majority
Empowerment Turnaround:
Improve the quality of life for women so they prefer to have few children – more education,
health, contraception, and opportunity
Food Turnaround:
Reduce the annual crop needed to feed everyone the diet they demand – more efficiency, less
waste, less red meat, more regenerative agriculture
Energy Turnaround:
Reduce the GHG emissions from the energy production that is needed to give everyone the energy
supply they demand – more efficiency, more electrification, more renewables, more CCS.
```

source: [methodology paper](https://eartharxiv.org/repository/view/5111/)

The former (TLTL) is described as the "base run", and appears to be their core implementation of system logic, with the latter (GL) being this core implementation plus the quoted "turnarounds". 

#### Other


