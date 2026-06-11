---
hide:
  - toc
---

This section describes one of the central concepts behind Delphos: the separation between dataset-specific modelling problems (Tasks) and the global modelling grammar (Catalogue).

While choice modellers interact with datasets, Delphos operates on a higher level of abstraction. Every dataset is transformed into a task representation, and all tasks are subsequently integrated into a common modelling grammar through the Catalogue.

This abstraction is what enables multitask learning and transfer learning across discrete choice modelling problems.

---

# Motivation

Suppose we wish to train Delphos on multiple transport datasets:

- Swissmetro
- LTDS
- ModeCanada
- Norway Value of Travel Time

Although these datasets differ in their variables, alternatives, sample sizes, and geographical contexts, they share many modelling concepts:

- Travel time
- Travel cost
- Socio-demographics
- Generic parameters
- Alternative-specific parameters
- Non-linear transformations

A reinforcement learning agent cannot directly reason about dataset-specific variable names such as:

text SM_TT

or

text rail_ivt

because these variables only exist in one dataset.

Instead, Delphos must learn at the level of modelling concepts.

The Task and Catalogue abstractions provide this capability.

---

# Task Representation

A Task represents a single discrete choice modelling problem.

Formally, a task can be viewed as:

$$
T=
(\mathcal{A},
\mathcal{X},
\mathcal{C},
\mathcal{F},
\mathcal{G})
$$

where:

- $\mathcal{A}$ denotes the alternatives.
- $\mathcal{X}$ denotes the attributes.
- $\mathcal{C}$ denotes the covariates.
- $\mathcal{F}$ denotes the available transformations.
- $\mathcal{G}$ denotes the available taste structures.

The task therefore defines the modelling space that Delphos is allowed to explore.

---

# Alternatives

Alternatives correspond to the available options within the choice set.

For example:

python task.alternatives

may produce:

python ( Alternative( id=1, name="car", choice=1, availability="av_car" ), Alternative( id=2, name="rail", choice=2, availability="av_rail" ), Alternative( id=3, name="swissmetro", choice=3, availability="av_sm" ) )

Each alternative contains:

| Field        | Description                |
| ------------ | -------------------------- |
| id           | Internal identifier        |
| name         | Human-readable name        |
| choice       | Choice code in the dataset |
| availability | Availability variable      |

---

# Attributes

Attributes define the explanatory variables available for model specification.

For example:

python task.get_attribute("travel_time")

may return:

python Attribute( id=2, name="travel_time", alternative={ 1: "car_tt", 2: "rail_tt", 3: "sm_tt" } )

The mapping specifies which dataset column corresponds to the attribute for each alternative.

From the perspective of Delphos, the attribute is represented only by its identifier:

$$
a_i
\in
\mathcal X
$$

regardless of the original variable names.

This abstraction is essential for transferring knowledge across datasets.

---

# Covariates

Covariates define variables that may interact with utility parameters.

For example:

python Covariate( id=1, name="income", levels=(0,1,2) )

The levels define the categories available for systematic taste heterogeneity.

A modelling term such as

$$
\beta_{TT}^{Income}
TT
$$

can therefore be represented internally as:

text (travel_time, linear, generic, income)

without referring to any dataset-specific coding.

---

# Transformations

Transformations determine how attributes enter the utility function.

Delphos currently supports:

python task.transform_names

python ( "linear", "log", "box_cox" )

These transformations correspond to:

$$
x
$$

$$
\log(x)
$$

$$
\frac{x^\lambda -1}{\lambda}
$$

respectively.

Transformations are represented using global identifiers and therefore remain consistent across tasks.

---

# Taste Structures

Taste structures determine whether parameters are shared across alternatives.

Delphos currently supports:

python ( "generic", "specific" )

A generic parameter:

$$
\beta_{TT}
$$

is shared across alternatives.

A specific parameter:

$$
\beta_{TT,j}
$$

is estimated separately for each alternative.

---

# Modelling Terms

The fundamental modelling unit used by Delphos is a modelling term.

Each term is represented as:

$$
t_i
=
(a_i,
\tau_i,
\gamma_i,
c_i)
$$

where:

- $a_i$ = attribute
- $\tau_i$ = transformation
- $\gamma_i$ = taste structure
- $c_i$ = interaction covariate

Examples:

text (travel_time, linear, generic, none) (travel_cost, log, generic, income) (headway, box_cox, specific, gender)

A utility specification is therefore represented as a set of modelling terms:

$$
S=
{
t_1,
t_2,
\ldots,
t_n
}
$$

rather than as executable utility equations.

This representation forms the state space of the reinforcement learning agent.

---

# Catalogue Construction

A Catalogue combines multiple tasks into a single global modelling grammar.

Suppose we have:

python catalogue = Catalogue.from_tasks( [ swissmetro, ltds, modecanada ] )

The catalogue aggregates all modelling concepts appearing across tasks.

Formally:

$$
A_{global}
=
\bigcup_{\tau}
A_\tau
$$

$$
C_{global}
=
\bigcup_{\tau}
C_\tau
$$

$$
F_{global}
=
\bigcup_{\tau}
F_\tau
$$

$$
G_{global}
=
\bigcup_{\tau}
G_\tau
$$

where $\tau$ indexes tasks.

---

# Global Identifiers

The catalogue assigns a unique identifier to every modelling concept.

For example:

python catalogue.global_attribute_ids

python (1,2,3,4,...,15)

Similarly:

python catalogue.global_covariate_ids catalogue.global_transform_ids catalogue.global_taste_ids

These identifiers define the modelling language used throughout Delphos.

The reinforcement learning agent never interacts with dataset-specific variable names.

Instead, it reasons entirely in terms of global identifiers.

---

# Task Masks

Not every modelling concept is available in every dataset.

For example:

text Swissmetro: Travel Time Travel Cost Headway LTDS: Travel Time Travel Cost Access Time

Consequently, Delphos uses task-specific masks.

For a task $\tau$:

$$
m_\tau
\in
{0,1}^{|A_{global}|}
$$

indicates which attributes are available.

For example:

python catalogue.attribute_mask(task)

might return:

python [1,1,1,0,0,0,1,0,...]

The same mechanism exists for:

- Attributes
- Covariates
- Transformations
- Taste structures

These masks ensure that the agent only proposes valid modelling operations.

---

# Why Tasks and Catalogue Matter

The Task and Catalogue abstractions are the foundation of Delphos' multitask learning framework.

Without them:

- Every dataset would require its own action space.
- States would have incompatible representations.
- Transfer learning would not be possible.

By introducing a global modelling grammar, Delphos can learn modelling patterns that generalise across datasets.

For example:

- Travel time often benefits from non-linear transformations.
- Cost variables frequently appear with generic parameters.
- Certain interactions repeatedly improve model fit.

These patterns can be transferred from one dataset to another because the Catalogue provides a shared representation.

---

# Summary

The Task abstraction describes an individual model specification problem.

The Catalogue combines multiple tasks into a shared modelling grammar.

Together they provide:

| Component       | Purpose                                         |
| --------------- | ----------------------------------------------- |
| Task            | Defines a dataset-specific modelling problem    |
| Alternative     | Represents a choice option                      |
| Attribute       | Represents explanatory variables                |
| Covariate       | Represents heterogeneity variables              |
| Transformation  | Defines functional forms                        |
| Taste Structure | Defines parameter sharing                       |
| Modelling Term  | Basic unit of model specification               |
| Catalogue       | Shared modelling grammar across tasks           |
| Task Masks      | Restrict modelling operations to valid concepts |

These abstractions form the basis of Delphos' representation learning and multitask reinforcement learning framework.

---

## Next Step

Continue to State Representation to understand how utility specifications are transformed into latent vectors that can be processed by the reinforcement learning agent.
