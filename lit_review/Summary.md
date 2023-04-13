# Summary document for literature review

N.B. Subject to being used as a scratchpad during lit review, to be whittled down and split out into more modular notes later.

## Key sources/forecasts

### Overview

From the Earth4All modelling study there is a great review of the main demographic modelling approaches in [the paper "People and Planet"](https://earth4all.life/wp-content/uploads/2023/04/E4A_People-and-Planet_Report.pdf) (section "2. Overview of main demographic approaches" TODO: link to paper TODO: link to paper).

This provides a great summary of the main forecast's approaches, somewhat condensed this frames them in the following way:

#### UN Population Division forecast: 

Purely statistical - uses time-series modelling to forecast population trends, essentially decouples population projections from impacts of policy (in keeping with UN neutral political stance).

Data-wise it collects "best available" demographic data and applies analytical instruments to correct/account for these. Bayesian hiearchical model used to infer fertility and mortality baselined (I presume? TODO: complete review of this paper) to 1950 population. This gives a computed uncertainty to forecast.

My distillation would be that this treats population as a function of several exogenous factors (its decoupled from any other dynamic factor).

### Forecasts and sources

Some of the main forecasts considered are here:

* [UN - Department of Economic and Social Affairs: Population Division](https://population.un.org/wpp/) - key for this study
* [Wittgenstein Centre (IIASA)](https://www.wittgensteincentre.org/en/index.htm)
* [Global Burden of Disease Study](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30677-2/fulltext) ([main link is pop forecast paper - this is project site](https://www.thelancet.com/gbd))
* [Institute for Health Metrics and Evaluation](https://www.healthdata.org/data-visualization/population-forecasting) - appears to be tied to Global Burden of Disease Study (project part of institute perhaps? Further reading needed)
* [World Bank](https://databank.worldbank.org/source/population-estimates-and-projections) So far [this is the closest thing to a methodology I've found](https://datahelpdesk.worldbank.org/knowledgebase/articles/843507-what-are-the-methodologies-used-in-estimating-the) but that looks like either there isn't any significant forecast or it's as simple as a linear regression against recent data (I think). UPDATE: [this gives a better picture of the methodology](https://datahelpdesk.worldbank.org/knowledgebase/articles/906531-methodologies)
* [DemographEye](https://worlddata.io/agespot-demographic-forecasts/) (looks like a local planning-specific tool but included on first pass as an attempt at completeness) - no obvious papers on methodology

These are the key ones I've found so far (will add any further to abive list).

#### UN Population division forecast

* Main resources here [UN - Department of Economic and Social Affairs: Population Division](https://population.un.org/wpp/)
* Cohort component projection (Leslie model with a migration term), non-constant fertility model (based on demographic transitions), more recently with a Bayesian inference model for fertility and mortality
* Well-established methodology with a lot of work done to account for obvserved non-trivial dynamics in fertility and mortality (c.f. demographic transitions)

#### World Bank forecast

Forecast methodology is described here (aside on content - this page shows a badly rendered equation: Xt = Xo (1 + r)t . = Xo (1 + r)t . = Xo (1 + r)t . is consistent with their claims if it is typeset as $x_t = x_0 (1 + r)^t$)

#### Wittgenstein Centre

#### Global Burden of Disease Study (& IHME?)

#### Earth4All projection

* Lots of papers/documentation but very complex model
* Great summary of state of art (TODO: put a link to where this is referenced later)


### Methodological sources

Currently storing these for review later - not necessarily all relevant

* [Bayesian Population Projections for the United Nations](https://arxiv.org/abs/1405.4708) - need to understand how this relates to current projections, also worth a look at authors and broader body of work (true for all refs here)
* [Bayesian Poisson Log-normal Model with Regularized Time Structure for Mortality Projection of Multi-population](https://arxiv.org/abs/2010.04775) - principally for looking at references
* [A Bayesian cohort component projection model to estimate adult populations at the subnational level in data-sparse settings](https://arxiv.org/abs/2102.06121)
* [The Probabilistic Explanation of the Cohort Component Population Projection Method](https://arxiv.org/abs/2109.13015) - hopefully helpful for better understanding uncertainties in CCPPM
* [Probabilistic Population Projections for Countries with Generalized HIV/AIDS Epidemics](https://arxiv.org/abs/1609.04383)
