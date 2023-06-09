# N8B Summary of forecast literature

<!-- toc -->

- [Key forecasts](#key-forecasts)
- [Description of key forecasts](#description-of-key-forecasts)
  * [United Nations Population Division: Population Prospects](#united-nations-population-division-population-prospects)
  * [Witgenstein Centre population projection](#witgenstein-centre-population-projection)
  * [Global Burden of Disease study (aka: Lancet model)](#global-burden-of-disease-study-aka-lancet-model)
  * [Earth4All model](#earth4all-model)

<!-- tocstop -->

This is a summary review of the information contained in other documents in this section. We briefly describe (and point to some useful high-level resources) main forecasts and key points related to later stages of the project.

For a much more detailed review and resource collection of population projections please see the DetailedNotes.md document in this folder (though note that these are organised as a collection of references and will be less readable).

## Key forecasts

We consider the following forecasts to be relevant to the project.

- United Nations Population Division: Population Prospects
- Witgenstein Centre population projection **(we drop the Wittgenstein centre prediction as unlike the other forecasts we have chosen this doesn't extend to 2100 and is therefore unlikely to forecast the next 8 billion births)**
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

[^1]: Strictly speaking there is an uncertainty on the data, which doesn't seem to be pulled into the prediction, I haven't found this addressed anywhere so seems reasonable to take this as assumed negligible.

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

UNPD projections account for these transitions using a model of their general structure. A more recent development was to refine curve fitting (parameter estimation)  in such a way that would also provide [the uncertainty mentioned above](#Uncertainty) ([Bayesian model described in this technical paper](https://arxiv.org/pdf/1405.4708.pdf)).

#### Key criticisms

The main criticism of the UNPD WPP projections is that they are pure time-series models, not accounting for anything but models of fertility and mortality (see [Lancet model paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2820%2930677-2/fulltext) and the [Earth4All People and Planet report](https://earth4all.life/wp-content/uploads/2023/04/E4A_People-and-Planet_Report.pdf)).

The other key criticism ([Lancet paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2820%2930677-2/fulltext)) is around assumptions about future behaviour, principally directed at migration assumptions (see previous section)

### Witgenstein Centre population projection

#### Overview

The Wittgenstein centre [have papers here,](https://www.jstor.org/stable/2695213?read-now=1&oauth_data=eyJlbWFpbCI6Im5pYWxsZmVhbHR5QGdvb2dsZW1haWwuY29tIiwiaW5zdGl0dXRpb25JZHMiOltdfQ&seq=11#page_scan_tab_contents) [and here](https://www.jstor.org/stable/26349563?seq=3) which make predictions from 2005-2050 with a model which was produced around this period (publication date in 2010).

This aside it doesn't seem to produce a regular projection which makes it somewhat ill-suited for our purposes -  mainly as the only available projection only goes out to 2050. Because of this we consider it as an important landmark in population projections and an important contributor but it does not provide a candidate data source.

#### Place in demographic modelling

The Wittgenstein projections form an important part of the context of demographic modelling for two key reasons

1. This was an early attempt to implement a model which accounted for external factors/policy decisions (the key addition was to incorporate education as a factor into the CCMP approach used by UNPD WPP) (see papers cited in [Overview](#overview-1))
2. The Wittgenstein Centre forecast is chosen for use in many climate models incorporating population-based factors (citation: [Lancet model paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2820%2930677-2/fulltext)) - though one criticism is that climate effects are not accounted for[^witt_crit].

[^witt_crit]: Side note - I'm inclined to take this criticism with a pinch of salt given that using a fixed forecast accounting for climate effects in a climate model would mean the population projection would be dependent on a different forecast (a messy and subtle situation to resolve), so it seems that the only sensible way to do this would be to produce a population model with a variable climate impact - i.e. produce a forecasting package replete with data...a very different task!

### Global Burden of Disease study (aka: Lancet model)

#### Overview

The Global Burden of Disease study is detailed [in this Lancet paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2820%2930677-2/fulltext) (hence the pseudonym).

As the name suggests this study is focused on understanding health impacts but also attempts to address its critiques of the Wittgenstein and UNPD WPP projections.

The Lancet paper claims a few improvements over UNPD and Wittgenstein (listed with some comments)

- Use more stable measure Completed Cohort Fertility at age 50 years (CCF50) "defined as the average number of children born to an individual female from an observed birth cohort if she lived to the end of her reproductive lifespan (age 15–49 years)" 
- This is then modelled as a function of educational attainment and contraceptive met need (which improves their model fit)
- Used a causal model to explore scenarios for these variables and impact on model - explicitly with the aim of exploring policy
- Applied future health scenarios to explore impact of education scenarios, a separate model for mortality from [this Lancet paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2818%2931694-5/fulltext) (to quote the paper: "This study provides a novel approach to modelling life expectancy, all-cause mortality and cause of death forecasts —and alternative future scenarios—for 250 causes of death from 2016 to 2040 in 195 countries and territories.")
- Built a time series model for migration modelling trends in Socio-demographic Index, crude population growth rate, and deaths from war and natural disasters
- Uncertainty is propagated from fertility, mortality and migration to predictions
- They also feed this population forecast into a GDP model

#### Data

Past UN data are used for migration model, other data are collected [here, on the Global Health Data eXchange](https://www.healthdata.org/data-tools-practices/data-sources). Without digging terribly deep (there doesn't appear to be a complete list provided) there seems to be a considerable overlap with sources used in UNPD WPP.

#### Uncertainty

The methodologies used admit (and explicitly state) an "error" term which can give a statistical measure of uncertainty. There are some commentaries on some of the results in the paper:

- The migration model (simple time-series model) has a very large uncertainty (while it accounts for a lot of variables this is not surprising heuristically given the complex nature of drivers of migration)
- Errors/CIs are clearly stated for all figures

#### Scenarios

From the Lancet paper
> In addition to the reference scenario, we developed four alternative scenarios that reflected faster or slower trajectories for two key drivers of fertility rates: education of females, and access to modern reproductive health services, measured by contraceptive met need.
> The slower, faster, and fastest alternate scenarios were derived by setting the annualised rate of change for education and contraceptive met need to their respective 15th, 85th, and 99th percentile rates of change across locations in the period 1990–2017. For the UN Sustainable Development Goal (SDG) pace alternate scenario, we set a rate of change to one that would allow all locations to meet the SDG targets for educational attainment (universal secondary education by 2030)
> and contraceptive met need (universal coverage by 2030).
> We held those rates constant past 2030 in the education SDG scenario, and held contraceptive met need at 100% coverage past 2030 (appendix 1, section 10). This scenario shows what we can expect population trends to look like if every country and territory meets the SDGs for education and contraceptive met need by 2030. Many countries are not on track to achieve these goals.

They specify several scenarios based on trajectories of multiple measures and have modelled the following:
- Reference scenario (base model, "vanilla" assumptions)
- Slower, faster, fastest and SDG contraceptive met need and female education trends

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


