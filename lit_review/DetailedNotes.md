# Summary document for literature review

N.B. Subject to being used as a scratchpad during lit review, to be whittled down and split out into more modular notes later.

<!-- toc -->

- [Key sources/forecasts](#key-sourcesforecasts)
  * [Overview](#overview)
    + [UN Population Division forecast:](#un-population-division-forecast)
    + [Wittgenstein Centre Approach](#wittgenstein-centre-approach)
    + [Lancet model](#lancet-model)
    + [Overall commentary](#overall-commentary)
  * [Forecasts and sources](#forecasts-and-sources)
  * [Observations and resources on key forecasts](#observations-and-resources-on-key-forecasts)
    + [UN Population division forecast](#un-population-division-forecast)
      - [Revisions to probabilistic forecast](#revisions-to-probabilistic-forecast)
    + [World Bank forecast](#world-bank-forecast)
    + [Wittgenstein Centre](#wittgenstein-centre)
    + [Global Burden of Disease Study/Lancet model](#global-burden-of-disease-studylancet-model)
      - [Improvements](#improvements)
    + [Earth4All projection](#earth4all-projection)
  * [Methodological sources](#methodological-sources)

<!-- tocstop -->

## Key sources/forecasts

### Overview

From the Earth4All modelling study there is a helpful review of the main demographic modelling approaches in [the paper "People and Planet"](https://earth4all.life/wp-content/uploads/2023/04/E4A_People-and-Planet_Report.pdf) (section "2. Overview of main demographic approaches").

This provides a great summary of the main forecast's approaches, somewhat condensed this frames them in the following way:

#### UN Population Division forecast: 

Purely statistical - uses time-series modelling to forecast population trends, essentially decouples population projections from impacts of policy (in keeping with UN neutral political stance).

Data-wise it collects "best available" demographic data and applies analytical instruments to correct/account for these. Bayesian hiearchical model used to infer fertility and mortality baselined (I presume? TODO: complete review of this paper) to 1950 population. This gives a computed uncertainty to forecast.

My distillation would be that this treats population as a function of several exogenous factors (its decoupled from any other dynamic factor).

#### Wittgenstein Centre Approach

Foundationally cohort component but generalised to include a model of interaction between future fertility, mortality, migration and education. Main motivation for adding in education is the theory/model assumption that it has a causal impact on fertility. Some open questions around causal impact, seems to be some inconsistency around observed trend (different for different stages of development).

E4A criticism seems to be focused around limitation of adding in causal effects and not accounting for further impacting factors (which seems consistent with the E4A chosen approach).


#### Lancet model

Described principally as adding further causes (health/contraception) which is incorporated in the form of a "cause-specific" mortality as a function of three factors - Socio-Demographic Index (SDI), "a risk-factor scalar that captures the combined risk factor effects for specific causes" and an ARIMA [though I suspect this could be the I(1) model mentioned later] to account for unexplained residual mortality. There is also a fertility model for no of children by the end of reproductive lifespan as a function of contraceptive met-need and female educational attainment. Finally net migration is modelled as a function of SDI, death due to conflict + natural disasters and diff between birth/death rates.

Lancet model also includes a mechanism connecting demographic and socio-demographic developments, calculating GDP of expected changes in national/global age structures.

#### Overall commentary

TODO: add image


### Forecasts and sources

The main forecasts considered are here:

* [UN - Department of Economic and Social Affairs: Population Division](https://population.un.org/wpp/) - key for this study
* [Wittgenstein Centre (IIASA)](https://www.wittgensteincentre.org/en/index.htm)
* Global Burden of Disease Study (referred to in some literature as **Lancet Model**) ([Pop. forecast paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30677-2/fulltext)) ([project site](https://www.thelancet.com/gbd)) [Institute for Health Metrics and Evaluation](https://www.healthdata.org/data-visualization/population-forecasting)
* [Earth4All model (link to publications page of project site)](https://earth4all.life/publications/)

Additionally the following were reviewed but not considered relevant to the study
* [World Bank](https://databank.worldbank.org/source/population-estimates-and-projections) Minimal information on methodology ([some minimal high level information here](https://datahelpdesk.worldbank.org/knowledgebase/articles/843507-what-are-the-methodologies-used-in-estimating-the), [deeper picture here but there seem to be some issues and open questions here](https://datahelpdesk.worldbank.org/knowledgebase/articles/906531-methodologies)
* [DemographEye](https://worlddata.io/agespot-demographic-forecasts/) (looks like a local planning-specific tool but included on first pass as an attempt at completeness) - no obvious papers on methodology (suspect this is proprietary) and doesn't seem targeted toward our questions.

### Observations and resources on key forecasts

#### UN Population division forecast

* Main resources here [UN - Department of Economic and Social Affairs: Population Division](https://population.un.org/wpp/)
* Cohort component projection (Leslie model with a migration term), non-constant fertility model (based on demographic transitions), more recently with a Bayesian inference model for fertility and mortality
* Well-established methodology with a lot of work done to account for obvserved non-trivial dynamics in fertility and mortality (c.f. demographic transitions)


##### Revisions to probabilistic forecast

[A 2014 article published by the UNPD](https://arxiv.org/pdf/1405.4708.pdf) was published to address concerns about long-term distribution of fertility (as well as the lack of any formal uncertainty bounds).

This gives a brief review of methodolgy from a mathematical modelling standpoint and then motivates the need for adding a Bayesian hierarchical model.



(n.b. this is also discussed [in this paper](https://www.researchgate.net/publication/51485137_Probabilistic_Projections_of_the_Total_Fertility_Rate_for_All_Countries), the historical context appears to be that the median scenario in this Bayesian projection was used as the medium scenario in the 2010 projection but I need to determine whether this methodology is the same)
#### World Bank forecast

Forecast methodology is described here (aside on content - this page shows a badly rendered equation: Xt = Xo (1 + r)t . = Xo (1 + r)t . = Xo (1 + r)t . is consistent with their claims if it is typeset as $x_t = x_0 (1 + r)^t$)

#### Wittgenstein Centre

#### Global Burden of Disease Study/Lancet model

[The Lancet paper is here](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2820%2930677-2/fulltext), lifting their methods section:

>We modelled future population in reference and alternative scenarios as a function of fertility, migration, and mortality rates. We developed statistical models for completed cohort fertility at age 50 years (CCF50). Completed cohort fertility is much more stable over time than the period measure of the total fertility rate (TFR). We modelled CCF50 as a time-series random walk function of educational attainment and contraceptive met need. Age-specific fertility rates were modelled as a function of CCF50 and covariates. We modelled age-specific mortality to 2100 using underlying mortality, a risk factor scalar, and an autoregressive integrated moving average (ARIMA) model. Net migration was modelled as a function of the Socio-demographic Index, crude population growth rate, and deaths from war and natural disasters; and use of an ARIMA model. The model framework was used to develop a reference scenario and alternative scenarios based on the pace of change in educational attainment and contraceptive met need. We estimated the size of gross domestic product for each country and territory in the reference scenario. Forecast uncertainty intervals (UIs) incorporated uncertainty propagated from past data inputs, model estimation, and forecast data distributions.

##### Improvements

The Lancet paper claims a few improvements over UNPD and Wittgenstein (listed with some comments)

- Use more stable measure Completed Cohort Fertility at age 50 years (CCF50) [TODO: simple explanation - I think this is essentially an aggregation of fertility but need to determine how this is applied in forecast]
- This is then modelled as a function of educational attainment and contraceptive met need (TODO: specifically?), which they claim accounts for 80.5% of variance (TODO: so $R^2 ~= 0.85$?)
- Used a causal model (TODO: regression?) to explore scenarios for these variables and impact on model - explicitly with the aim of exploring policy
- Applied future health scenarios (TODO: published by same group?) to explore impact of ed. scenarios, this essentially forms a separate model for mortality
- Built a time series model for migration modelling trends in Socio-demographic Index, crude population growth rate, and deaths from war and natural disasters
- Uncertainty is propagated from fertility, mortality and migration to predictions (TODO: I thought this was available for at least UNPD...?)
- Wording isn't totally clear (TODO: figure out this one) but they appear to compute the impact of GDP on population? (alternatively they may be working out the expected impact on GDP of population changes..)

#### Earth4All projection

* Lots of papers/documentation but very complex model
* Based on a systems dynamical modelling approach it models a system with interacting parts rather than trying to separate out population from factors which impact population. So for example population will have an impact on (e.g.) GDP, global warming, which will then in turn have an impact on population according to the logic of the model
* Designed for use in unerstanding the impact of policy decisions and actions on people around the World
* A lot of documentation available but due to comlexity of models there isn't a single straightforward methodology paper, there is a lot of methodology spread across multiple papers and plans to continue publishing work on their methodology
* From current literature some highlights are
  * [Exec summary](https://earth4all.life/wp-content/uploads/2023/03/Earth4All_Exec_Summary_EN.pdf) - covers high level results and some of the scenario context/high level picture of modelling decisions
  * [People and planet report](https://earth4all.life/wp-content/uploads/2023/04/E4A_People-and-Planet_Report.pdf) - source of summaries of UNPD/Wittgenstein/Lancet model above, covers a lot of analysis driving population components
  * A preprint of the modelling is available [through this portal](https://eartharxiv.org/repository/view/5111/) which gives some of the technical detail on modelling
* Great summary of state of art (see descriptions above)

To give a clearer picture of the way the system is constructed we include the following diagrams showing how these sub-systems interact

![High level schematic](https://github.com/Niallfealty/n8b_un_foundation/blob/main/lit_review/images/Earth4All_major_sectors_diagram.png)

For a more detailed picture we also include the following more complex diagram

![Low level detail](https://github.com/Niallfealty/n8b_un_foundation/blob/main/lit_review/images/model_causal_diagram.png)

### Methodological sources

Currently storing these for review later - not necessarily all relevant

* [Bayesian Population Projections for the United Nations](https://arxiv.org/abs/1405.4708) - need to understand how this relates to current projections, also worth a look at authors and broader body of work (true for all refs here)
* [Bayesian Poisson Log-normal Model with Regularized Time Structure for Mortality Projection of Multi-population](https://arxiv.org/abs/2010.04775) - principally for looking at references
* [A Bayesian cohort component projection model to estimate adult populations at the subnational level in data-sparse settings](https://arxiv.org/abs/2102.06121)
* [The Probabilistic Explanation of the Cohort Component Population Projection Method](https://arxiv.org/abs/2109.13015) - hopefully helpful for better understanding uncertainties in CCPPM
* [Probabilistic Population Projections for Countries with Generalized HIV/AIDS Epidemics](https://arxiv.org/abs/1609.04383)
