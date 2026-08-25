---
hide:
  - toc
---
# 06 - Quick results

This recipe is for a first practical run. It keeps the modelling space small, proposes a modest number of models, and optionally estimates them with Apollo/R.


## 1. Quick-run settings



```python
import delphos as dp

RUN_ESTIMATION = True
OUTPUT_CSV = "quick_results.csv"

agent = dp.load_agent()
task = dp.load_dataset("Swissmetro")

```

## 2. Keep the search space compact

Start with transformations and tastes, but no covariates. This usually gives interpretable first models.



```python
quick_task = dp.configure_modelling_space(
    task,
    transformations=["linear", "log"],
    tastes=["generic", "specific"],
    covariates=[],
)

print("Attributes:", quick_task.attribute_names)
print("Transformations:", quick_task.transform_names)
print("Tastes:", quick_task.taste_names)
print("Covariates:", quick_task.covariate_names)

```

    Attributes: ('ASC', 'time', 'cost', 'headway', 'seat')
    Transformations: ('linear', 'log')
    Tastes: ('generic', 'specific')
    Covariates: ()


## 3. Generate specifications



```python
models = agent.propose(
    quick_task,
    n_models=20,
    max_attempts=500,
    seed=2026,
)

df = models.to_dataframe()


if RUN_ESTIMATION:
    models.estimate(
        quick_task,
        max_free_parameters=50,
        info=True,
        save=False,
    )
    df = models.to_dataframe()

df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved results to {OUTPUT_CSV}")

```

    2026-07-06 08:39:48,955 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2210_3210_4120_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2210_3210_4120_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:49.036085
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -8.756216
         reciprocal of condition number         : 0.0041998
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -5207.86
    Rho-squared vs equal shares                  :  0.2522 
    Adj.Rho-squared vs equal shares              :  0.2512 
    Rho-squared vs observed shares               :  0.112 
    Adj.Rho-squared vs observed shares           :  0.1112 
    AIC                                         :  10429.72 
    BIC                                         :  10477.46 
    
    Estimated parameters                        : 7
    Time taken (hh:mm:ss)                       :  00:00:0.42 
         pre-estimation                         :  00:00:0.09 
         estimation                             :  00:00:0.19 
         post-estimation                        :  00:00:0.15 
    Iterations                                  :  11  
    
    Unconstrained optimisation.
    
    Estimates:
                          Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN              -0.2077     0.08072      -2.573      0.1184
    ASC_SM                  0.1801     0.08198       2.197      0.1203
    ASC_CAR                 0.0000          NA          NA          NA
    b_time_generic_log     -3.4175     0.14359     -23.800      0.3659
    b_cost_generic_log     -2.7007     0.11991     -22.523      0.3233
    b_TRAIN_headway        -0.5065     0.10122      -5.004      0.1129
    b_SM_headway           -0.7205     0.33120      -2.175      0.2664
    b_SM_seat_log          -0.6055     0.12464      -4.858      0.2190
                       Rob.t.rat.(0)
    ASC_TRAIN                 -1.754
    ASC_SM                     1.497
    ASC_CAR                       NA
    b_time_generic_log        -9.339
    b_cost_generic_log        -8.354
    b_TRAIN_headway           -4.485
    b_SM_headway              -2.705
    b_SM_seat_log             -2.765
    
    2026-07-06 08:39:49,514 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2220_3120_4210_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2220_3120_4210_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:49.552798
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -12.148235
         reciprocal of condition number         : 0.00244169
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4990.1
    Rho-squared vs equal shares                  :  0.2835 
    Adj.Rho-squared vs equal shares              :  0.2821 
    Rho-squared vs observed shares               :  0.1492 
    Adj.Rho-squared vs observed shares           :  0.1478 
    AIC                                         :  10000.2 
    BIC                                         :  10068.4 
    
    Estimated parameters                        : 10
    Time taken (hh:mm:ss)                       :  00:00:0.48 
         pre-estimation                         :  00:00:0.08 
         estimation                             :  00:00:0.1 
         post-estimation                        :  00:00:0.3 
    Iterations                                  :  15  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  0.7835     0.19527       4.012      0.4433
    ASC_SM                     0.1568     0.12593       1.245      0.2871
    ASC_CAR                    0.0000          NA          NA          NA
    b_TRAIN_time_log          -2.9470     0.21418     -13.759      0.5592
    b_SM_time_log             -3.0526     0.17866     -17.087      0.5004
    b_CAR_time_log            -3.6254     0.20211     -17.938      0.4736
    b_TRAIN_cost              -3.0814     0.12028     -25.617      0.4483
    b_SM_cost                 -1.1384     0.05512     -20.654      0.1883
    b_CAR_cost                -0.8043     0.10771      -7.467      0.1982
    b_headway_generic_log     -0.8857     0.16405      -5.399      0.1758
    b_seat_generic            -0.1102     0.08761      -1.257      0.1395
                          Rob.t.rat.(0)
    ASC_TRAIN                    1.7674
    ASC_SM                       0.5459
    ASC_CAR                          NA
    b_TRAIN_time_log            -5.2700
    b_SM_time_log               -6.1001
    b_CAR_time_log              -7.6541
    b_TRAIN_cost                -6.8728
    b_SM_cost                   -6.0454
    b_CAR_cost                  -4.0584
    b_headway_generic_log       -5.0368
    b_seat_generic              -0.7896
    
    2026-07-06 08:39:50,103 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2220_3120_4210_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2220_3120_4210_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:50.138321
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -12.148178
         reciprocal of condition number         : 0.00244377
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4990.1
    Rho-squared vs equal shares                  :  0.2835 
    Adj.Rho-squared vs equal shares              :  0.2821 
    Rho-squared vs observed shares               :  0.1492 
    Adj.Rho-squared vs observed shares           :  0.1478 
    AIC                                         :  10000.2 
    BIC                                         :  10068.4 
    
    Estimated parameters                        : 10
    Time taken (hh:mm:ss)                       :  00:00:0.47 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.1 
         post-estimation                        :  00:00:0.3 
    Iterations                                  :  15  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  0.7835     0.19527       4.012      0.4433
    ASC_SM                     0.1568     0.12593       1.245      0.2871
    ASC_CAR                    0.0000          NA          NA          NA
    b_TRAIN_time_log          -2.9470     0.21418     -13.759      0.5592
    b_SM_time_log             -3.0526     0.17866     -17.087      0.5004
    b_CAR_time_log            -3.6254     0.20211     -17.938      0.4736
    b_TRAIN_cost              -3.0814     0.12028     -25.617      0.4483
    b_SM_cost                 -1.1384     0.05512     -20.654      0.1883
    b_CAR_cost                -0.8043     0.10771      -7.467      0.1982
    b_headway_generic_log     -0.8857     0.16405      -5.399      0.1758
    b_SM_seat_log             -0.1589     0.12640      -1.257      0.2013
                          Rob.t.rat.(0)
    ASC_TRAIN                    1.7674
    ASC_SM                       0.5459
    ASC_CAR                          NA
    b_TRAIN_time_log            -5.2700
    b_SM_time_log               -6.1001
    b_CAR_time_log              -7.6541
    b_TRAIN_cost                -6.8728
    b_SM_cost                   -6.0454
    b_CAR_cost                  -4.0584
    b_headway_generic_log       -5.0368
    b_SM_seat_log               -0.7896
    
    2026-07-06 08:39:50,717 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2220_3210_4210_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2220_3210_4210_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:50.760393
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -13.153366
         reciprocal of condition number         : 0.00495437
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -5172.77
    Rho-squared vs equal shares                  :  0.2573 
    Adj.Rho-squared vs equal shares              :  0.2561 
    Rho-squared vs observed shares               :  0.118 
    Adj.Rho-squared vs observed shares           :  0.117 
    AIC                                         :  10361.54 
    BIC                                         :  10416.1 
    
    Estimated parameters                        : 8
    Time taken (hh:mm:ss)                       :  00:00:0.35 
         pre-estimation                         :  00:00:0.09 
         estimation                             :  00:00:0.08 
         post-estimation                        :  00:00:0.18 
    Iterations                                  :  11  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  1.1371      0.1871       6.078      0.4053
    ASC_SM                     0.3944      0.1257       3.138      0.2798
    ASC_CAR                    0.0000          NA          NA          NA
    b_TRAIN_time_log          -4.4994      0.1975     -22.785      0.4905
    b_SM_time_log             -3.2250      0.1798     -17.936      0.5269
    b_CAR_time_log            -3.0336      0.1569     -19.331      0.3541
    b_cost_generic_log        -2.6846      0.1191     -22.547      0.3143
    b_headway_generic_log     -0.8618      0.1599      -5.390      0.1745
    b_SM_seat_log             -0.5252      0.1263      -4.159      0.2191
                          Rob.t.rat.(0)
    ASC_TRAIN                     2.806
    ASC_SM                        1.410
    ASC_CAR                          NA
    b_TRAIN_time_log             -9.173
    b_SM_time_log                -6.121
    b_CAR_time_log               -8.567
    b_cost_generic_log           -8.543
    b_headway_generic_log        -4.938
    b_SM_seat_log                -2.398
    
    2026-07-06 08:39:51,197 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2220_3120_4110_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2220_3120_4110_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:51.266144
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -12.369941
         reciprocal of condition number         : 0.0024867
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4990.34
    Rho-squared vs equal shares                  :  0.2835 
    Adj.Rho-squared vs equal shares              :  0.282 
    Rho-squared vs observed shares               :  0.1491 
    Adj.Rho-squared vs observed shares           :  0.1478 
    AIC                                         :  10000.68 
    BIC                                         :  10068.88 
    
    Estimated parameters                        : 10
    Time taken (hh:mm:ss)                       :  00:00:0.41 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.1 
         post-estimation                        :  00:00:0.23 
    Iterations                                  :  15  
    
    Unconstrained optimisation.
    
    Estimates:
                         Estimate        s.e.   t.rat.(0)    Rob.s.e. Rob.t.rat.(0)
    ASC_TRAIN              0.7100     0.19058      3.7253      0.4407        1.6110
    ASC_SM                 0.1049     0.12420      0.8443      0.2859        0.3667
    ASC_CAR                0.0000          NA          NA          NA            NA
    b_TRAIN_time_log      -2.9469     0.21415    -13.7610      0.5589       -5.2724
    b_SM_time_log         -3.0517     0.17862    -17.0852      0.5002       -6.1009
    b_CAR_time_log        -3.6269     0.20222    -17.9355      0.4741       -7.6499
    b_TRAIN_cost          -3.0809     0.12027    -25.6176      0.4482       -6.8742
    b_SM_cost             -1.1380     0.05511    -20.6503      0.1883       -6.0451
    b_CAR_cost            -0.8013     0.10773     -7.4375      0.1982       -4.0417
    b_headway_generic     -0.5370     0.10061     -5.3371      0.1102       -4.8718
    b_seat_generic        -0.1097     0.08763     -1.2517      0.1396       -0.7857
    
    2026-07-06 08:39:51,723 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2220_3210_4110_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2220_3210_4110_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:51.758617
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -13.382018
         reciprocal of condition number         : 0.00498837
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -5173.14
    Rho-squared vs equal shares                  :  0.2572 
    Adj.Rho-squared vs equal shares              :  0.2561 
    Rho-squared vs observed shares               :  0.118 
    Adj.Rho-squared vs observed shares           :  0.1169 
    AIC                                         :  10362.28 
    BIC                                         :  10416.84 
    
    Estimated parameters                        : 8
    Time taken (hh:mm:ss)                       :  00:00:0.4 
         pre-estimation                         :  00:00:0.08 
         estimation                             :  00:00:0.09 
         post-estimation                        :  00:00:0.24 
    Iterations                                  :  11  
    
    Unconstrained optimisation.
    
    Estimates:
                          Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN               1.0628     0.18237       5.828      0.4026
    ASC_SM                  0.3435     0.12408       2.769      0.2784
    ASC_CAR                 0.0000          NA          NA          NA
    b_TRAIN_time_log       -4.4982     0.19749     -22.777      0.4905
    b_SM_time_log          -3.2236     0.17978     -17.931      0.5267
    b_CAR_time_log         -3.0311     0.15690     -19.319      0.3540
    b_cost_generic_log     -2.6833     0.11905     -22.539      0.3141
    b_headway_generic      -0.5181     0.09772      -5.302      0.1089
    b_seat_generic         -0.3629     0.08755      -4.145      0.1519
                       Rob.t.rat.(0)
    ASC_TRAIN                  2.640
    ASC_SM                     1.234
    ASC_CAR                       NA
    b_TRAIN_time_log          -9.170
    b_SM_time_log             -6.121
    b_CAR_time_log            -8.563
    b_cost_generic_log        -8.542
    b_headway_generic         -4.757
    b_seat_generic            -2.388
    
    2026-07-06 08:39:52,210 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2120_3210_4110_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2120_3210_4110_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:52.245876
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -36.89858
         reciprocal of condition number         : 0.0086079
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -5244.05
    Rho-squared vs equal shares                  :  0.247 
    Adj.Rho-squared vs equal shares              :  0.2459 
    Rho-squared vs observed shares               :  0.1059 
    Adj.Rho-squared vs observed shares           :  0.1049 
    AIC                                         :  10504.1 
    BIC                                         :  10558.66 
    
    Estimated parameters                        : 8
    Time taken (hh:mm:ss)                       :  00:00:0.33 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.09 
         post-estimation                        :  00:00:0.17 
    Iterations                                  :  18  
    
    Unconstrained optimisation.
    
    Estimates:
                          Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN               0.4073     0.13611       2.992      0.3177
    ASC_SM                  0.5424     0.09150       5.927      0.2825
    ASC_CAR                 0.0000          NA          NA          NA
    b_TRAIN_time           -1.5228     0.07786     -19.559      0.2722
    b_SM_time              -1.2042     0.08729     -13.794      0.4991
    b_CAR_time             -1.0390     0.06217     -16.712      0.2250
    b_cost_generic_log     -2.6551     0.11791     -22.517      0.3085
    b_headway_generic      -0.5226     0.09727      -5.373      0.1078
    b_SM_seat_log          -0.5447     0.12506      -4.355      0.2187
                       Rob.t.rat.(0)
    ASC_TRAIN                  1.282
    ASC_SM                     1.920
    ASC_CAR                       NA
    b_TRAIN_time              -5.594
    b_SM_time                 -2.412
    b_CAR_time                -4.617
    b_cost_generic_log        -8.606
    b_headway_generic         -4.845
    b_SM_seat_log             -2.490
    
    2026-07-06 08:39:52,631 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2210_3120_4110_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2210_3120_4110_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:52.686268
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -36.876817
         reciprocal of condition number         : 0.00918761
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4994.54
    Rho-squared vs equal shares                  :  0.2829 
    Adj.Rho-squared vs equal shares              :  0.2817 
    Rho-squared vs observed shares               :  0.1484 
    Adj.Rho-squared vs observed shares           :  0.1474 
    AIC                                         :  10005.08 
    BIC                                         :  10059.64 
    
    Estimated parameters                        : 8
    Time taken (hh:mm:ss)                       :  00:00:0.55 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.19 
         post-estimation                        :  00:00:0.29 
    Iterations                                  :  20  
    
    Unconstrained optimisation.
    
    Estimates:
                          Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN               1.0793     0.11601       9.303      0.2347
    ASC_SM                  0.3474     0.08178       4.247      0.1577
    ASC_CAR                 0.0000          NA          NA          NA
    b_time_generic_log     -3.2424     0.14949     -21.690      0.3909
    b_TRAIN_cost           -2.9996     0.11327     -26.482      0.3908
    b_SM_cost              -1.1036     0.05335     -20.687      0.1693
    b_CAR_cost             -0.9729     0.08979     -10.836      0.2241
    b_headway_generic      -0.5360     0.10075      -5.320      0.1108
    b_seat_generic         -0.1208     0.08728      -1.384      0.1393
                       Rob.t.rat.(0)
    ASC_TRAIN                 4.5986
    ASC_SM                    2.2030
    ASC_CAR                       NA
    b_time_generic_log       -8.2945
    b_TRAIN_cost             -7.6754
    b_SM_cost                -6.5176
    b_CAR_cost               -4.3411
    b_headway_generic        -4.8369
    b_seat_generic           -0.8666
    
    2026-07-06 08:39:53,317 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2220_3220_4120_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2220_3220_4120_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:53.361843
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -8.851345
         reciprocal of condition number         : 0.00245889
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4904.43
    Rho-squared vs equal shares                  :  0.2958 
    Adj.Rho-squared vs equal shares              :  0.2942 
    Rho-squared vs observed shares               :  0.1638 
    Adj.Rho-squared vs observed shares           :  0.1622 
    AIC                                         :  9830.86 
    BIC                                         :  9905.88 
    
    Estimated parameters                        : 11
    Time taken (hh:mm:ss)                       :  00:00:0.53 
         pre-estimation                         :  00:00:0.08 
         estimation                             :  00:00:0.12 
         post-estimation                        :  00:00:0.33 
    Iterations                                  :  17  
    
    Unconstrained optimisation.
    
    Estimates:
                        Estimate        s.e.   t.rat.(0)    Rob.s.e. Rob.t.rat.(0)
    ASC_TRAIN             1.0579      0.1949       5.428      0.4424        2.3914
    ASC_SM                0.4574      0.1409       3.247      0.2769        1.6517
    ASC_CAR               0.0000          NA          NA          NA            NA
    b_TRAIN_time_log     -2.8187      0.2152     -13.100      0.5601       -5.0325
    b_SM_time_log        -3.0361      0.1801     -16.858      0.5088       -5.9671
    b_CAR_time_log       -3.7802      0.2100     -18.003      0.4854       -7.7880
    b_TRAIN_cost_log     -6.1096      0.2078     -29.395      0.6454       -9.4660
    b_SM_cost_log        -2.8810      0.1309     -22.005      0.3933       -7.3257
    b_CAR_cost_log       -1.6689      0.2234      -7.470      0.4178       -3.9949
    b_TRAIN_headway      -0.5286      0.1077      -4.906      0.1215       -4.3489
    b_SM_headway         -0.6931      0.3282      -2.112      0.2583       -2.6828
    b_SM_seat_log        -0.1660      0.1273      -1.304      0.2030       -0.8179
    
    2026-07-06 08:39:53,953 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2120_3220_4110_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2120_3220_4110_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:53.989782
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -16.333378
         reciprocal of condition number         : 0.00309193
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4976.42
    Rho-squared vs equal shares                  :  0.2855 
    Adj.Rho-squared vs equal shares              :  0.284 
    Rho-squared vs observed shares               :  0.1515 
    Adj.Rho-squared vs observed shares           :  0.1501 
    AIC                                         :  9972.84 
    BIC                                         :  10041.04 
    
    Estimated parameters                        : 10
    Time taken (hh:mm:ss)                       :  00:00:0.56 
         pre-estimation                         :  00:00:0.11 
         estimation                             :  00:00:0.13 
         post-estimation                        :  00:00:0.32 
    Iterations                                  :  22  
    
    Unconstrained optimisation.
    
    Estimates:
                         Estimate        s.e.   t.rat.(0)    Rob.s.e. Rob.t.rat.(0)
    ASC_TRAIN              1.0663     0.15187       7.021      0.3219        3.3126
    ASC_SM                 0.8528     0.10919       7.810      0.2545        3.3511
    ASC_CAR                0.0000          NA          NA          NA            NA
    b_TRAIN_time          -0.8315     0.08311     -10.005      0.2981       -2.7892
    b_SM_time             -1.1073     0.08766     -12.632      0.4957       -2.2340
    b_CAR_time            -1.3044     0.08207     -15.894      0.2978       -4.3802
    b_TRAIN_cost_log      -6.0531     0.20592     -29.396      0.6363       -9.5130
    b_SM_cost_log         -2.8304     0.12906     -21.932      0.3898       -7.2621
    b_CAR_cost_log        -1.7213     0.21740      -7.917      0.5322       -3.2340
    b_headway_generic     -0.5538     0.10134      -5.464      0.1116       -4.9622
    b_seat_generic        -0.1345     0.08740      -1.539      0.1386       -0.9708
    
    2026-07-06 08:39:54,603 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2210_3120_4120_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2210_3120_4120_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:54.642104
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -8.980172
         reciprocal of condition number         : 0.0021914
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4994.39
    Rho-squared vs equal shares                  :  0.2829 
    Adj.Rho-squared vs equal shares              :  0.2816 
    Rho-squared vs observed shares               :  0.1484 
    Adj.Rho-squared vs observed shares           :  0.1472 
    AIC                                         :  10006.78 
    BIC                                         :  10068.16 
    
    Estimated parameters                        : 9
    Time taken (hh:mm:ss)                       :  00:00:0.38 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.11 
         post-estimation                        :  00:00:0.2 
    Iterations                                  :  18  
    
    Unconstrained optimisation.
    
    Estimates:
                          Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN               1.0662     0.11851       8.997      0.2375
    ASC_SM                  0.3801     0.10181       3.734      0.1612
    ASC_CAR                 0.0000          NA          NA          NA
    b_time_generic_log     -3.2426     0.14947     -21.693      0.3908
    b_TRAIN_cost           -3.0001     0.11327     -26.486      0.3908
    b_SM_cost              -1.1039     0.05336     -20.689      0.1693
    b_CAR_cost             -0.9746     0.08985     -10.847      0.2242
    b_TRAIN_headway        -0.5172     0.10644      -4.859      0.1197
    b_SM_headway           -0.7043     0.32725      -2.152      0.2572
    b_SM_seat_log          -0.1743     0.12591      -1.384      0.2011
                       Rob.t.rat.(0)
    ASC_TRAIN                 4.4900
    ASC_SM                    2.3575
    ASC_CAR                       NA
    b_time_generic_log       -8.2972
    b_TRAIN_cost             -7.6760
    b_SM_cost                -6.5187
    b_CAR_cost               -4.3469
    b_TRAIN_headway          -4.3215
    b_SM_headway             -2.7388
    b_SM_seat_log            -0.8669
    
    2026-07-06 08:39:55,148 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2210_3120_4210_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2210_3120_4210_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:55.191693
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -26.123761
         reciprocal of condition number         : 0.00650691
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4994.27
    Rho-squared vs equal shares                  :  0.2829 
    Adj.Rho-squared vs equal shares              :  0.2818 
    Rho-squared vs observed shares               :  0.1485 
    Adj.Rho-squared vs observed shares           :  0.1474 
    AIC                                         :  10004.55 
    BIC                                         :  10059.1 
    
    Estimated parameters                        : 8
    Time taken (hh:mm:ss)                       :  00:00:0.4 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.09 
         post-estimation                        :  00:00:0.24 
    Iterations                                  :  14  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  1.1525     0.12365       9.321      0.2376
    ASC_SM                     0.3983     0.08432       4.723      0.1592
    ASC_CAR                    0.0000          NA          NA          NA
    b_time_generic_log        -3.2425     0.14948     -21.692      0.3908
    b_TRAIN_cost              -3.0000     0.11327     -26.485      0.3908
    b_SM_cost                 -1.1040     0.05335     -20.693      0.1694
    b_CAR_cost                -0.9752     0.08981     -10.859      0.2242
    b_headway_generic_log     -0.8848     0.16426      -5.387      0.1767
    b_seat_generic            -0.1213     0.08727      -1.389      0.1393
                          Rob.t.rat.(0)
    ASC_TRAIN                    4.8501
    ASC_SM                       2.5017
    ASC_CAR                          NA
    b_time_generic_log          -8.2965
    b_TRAIN_cost                -7.6758
    b_SM_cost                   -6.5185
    b_CAR_cost                  -4.3501
    b_headway_generic_log       -5.0067
    b_seat_generic              -0.8706
    
    2026-07-06 08:39:55,642 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2120_3120_4210_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2120_3120_4210_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:55.678493
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -24.824719
         reciprocal of condition number         : 0.00364464
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -5059.2
    Rho-squared vs equal shares                  :  0.2736 
    Adj.Rho-squared vs equal shares              :  0.2722 
    Rho-squared vs observed shares               :  0.1374 
    Adj.Rho-squared vs observed shares           :  0.136 
    AIC                                         :  10138.41 
    BIC                                         :  10206.61 
    
    Estimated parameters                        : 10
    Time taken (hh:mm:ss)                       :  00:00:0.62 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.23 
         post-estimation                        :  00:00:0.32 
    Iterations                                  :  37  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  0.7044     0.14712       4.788      0.3230
    ASC_SM                     0.5448     0.09527       5.718      0.2619
    ASC_CAR                    0.0000          NA          NA          NA
    b_TRAIN_time              -0.8786     0.08309     -10.574      0.2947
    b_SM_time                 -1.1132     0.08715     -12.773      0.4896
    b_CAR_time                -1.2815     0.08064     -15.891      0.2932
    b_TRAIN_cost              -3.0719     0.11968     -25.667      0.4450
    b_SM_cost                 -1.1298     0.05470     -20.654      0.1898
    b_CAR_cost                -0.7961     0.10612      -7.502      0.2470
    b_headway_generic_log     -0.8962     0.16328      -5.489      0.1745
    b_seat_generic            -0.1295     0.08678      -1.492      0.1380
                          Rob.t.rat.(0)
    ASC_TRAIN                    2.1808
    ASC_SM                       2.0804
    ASC_CAR                          NA
    b_TRAIN_time                -2.9816
    b_SM_time                   -2.2738
    b_CAR_time                  -4.3715
    b_TRAIN_cost                -6.9035
    b_SM_cost                   -5.9538
    b_CAR_cost                  -3.2227
    b_headway_generic_log       -5.1365
    b_seat_generic              -0.9380
    
    2026-07-06 08:39:56,390 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2120_3220_4110_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2120_3220_4110_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:56.427379
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -16.331039
         reciprocal of condition number         : 0.00309456
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4976.42
    Rho-squared vs equal shares                  :  0.2855 
    Adj.Rho-squared vs equal shares              :  0.284 
    Rho-squared vs observed shares               :  0.1515 
    Adj.Rho-squared vs observed shares           :  0.1501 
    AIC                                         :  9972.84 
    BIC                                         :  10041.04 
    
    Estimated parameters                        : 10
    Time taken (hh:mm:ss)                       :  00:00:0.5 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.14 
         post-estimation                        :  00:00:0.3 
    Iterations                                  :  22  
    
    Unconstrained optimisation.
    
    Estimates:
                         Estimate        s.e.   t.rat.(0)    Rob.s.e. Rob.t.rat.(0)
    ASC_TRAIN              1.0663     0.15187       7.021      0.3219        3.3126
    ASC_SM                 0.8528     0.10919       7.810      0.2545        3.3511
    ASC_CAR                0.0000          NA          NA          NA            NA
    b_TRAIN_time          -0.8315     0.08311     -10.005      0.2981       -2.7892
    b_SM_time             -1.1073     0.08766     -12.632      0.4957       -2.2340
    b_CAR_time            -1.3044     0.08207     -15.894      0.2978       -4.3802
    b_TRAIN_cost_log      -6.0531     0.20592     -29.396      0.6363       -9.5130
    b_SM_cost_log         -2.8304     0.12906     -21.932      0.3898       -7.2621
    b_CAR_cost_log        -1.7213     0.21740      -7.917      0.5322       -3.2340
    b_headway_generic     -0.5538     0.10134      -5.464      0.1116       -4.9622
    b_SM_seat_log         -0.1941     0.12609      -1.539      0.1999       -0.9708
    
    2026-07-06 08:39:57,005 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2210_3220_4120_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2210_3220_4120_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:57.050945
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -8.931856
         reciprocal of condition number         : 0.00335113
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4911.51
    Rho-squared vs equal shares                  :  0.2948 
    Adj.Rho-squared vs equal shares              :  0.2935 
    Rho-squared vs observed shares               :  0.1626 
    Adj.Rho-squared vs observed shares           :  0.1614 
    AIC                                         :  9841.01 
    BIC                                         :  9902.39 
    
    Estimated parameters                        : 9
    Time taken (hh:mm:ss)                       :  00:00:0.44 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.08 
         post-estimation                        :  00:00:0.28 
    Iterations                                  :  13  
    
    Unconstrained optimisation.
    
    Estimates:
                          Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN               1.4888      0.1396      10.663      0.2717
    ASC_SM                  0.6670      0.1221       5.460      0.2068
    ASC_CAR                 0.0000          NA          NA          NA
    b_time_generic_log     -3.2566      0.1504     -21.652      0.3956
    b_TRAIN_cost_log       -5.9102      0.1973     -29.960      0.5559
    b_SM_cost_log          -2.7784      0.1265     -21.959      0.3470
    b_CAR_cost_log         -2.1369      0.1808     -11.822      0.4449
    b_TRAIN_headway        -0.5255      0.1079      -4.869      0.1225
    b_SM_headway           -0.7036      0.3278      -2.146      0.2575
    b_SM_seat_log          -0.1760      0.1269      -1.387      0.2023
                       Rob.t.rat.(0)
    ASC_TRAIN                 5.4801
    ASC_SM                    3.2246
    ASC_CAR                       NA
    b_time_generic_log       -8.2324
    b_TRAIN_cost_log        -10.6313
    b_SM_cost_log            -8.0073
    b_CAR_cost_log           -4.8034
    b_TRAIN_headway          -4.2886
    b_SM_headway             -2.7321
    b_SM_seat_log            -0.8701
    
    2026-07-06 08:39:57,616 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2210_3220_4210_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2210_3220_4210_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:57.652613
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -16.71243
         reciprocal of condition number         : 0.00665264
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4911.39
    Rho-squared vs equal shares                  :  0.2948 
    Adj.Rho-squared vs equal shares              :  0.2937 
    Rho-squared vs observed shares               :  0.1626 
    Adj.Rho-squared vs observed shares           :  0.1616 
    AIC                                         :  9838.79 
    BIC                                         :  9893.35 
    
    Estimated parameters                        : 8
    Time taken (hh:mm:ss)                       :  00:00:0.4 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.15 
         post-estimation                        :  00:00:0.17 
    Iterations                                  :  13  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  1.5749      0.1438      10.949      0.2715
    ASC_SM                     0.6872      0.1082       6.350      0.2053
    ASC_CAR                    0.0000          NA          NA          NA
    b_time_generic_log        -3.2565      0.1504     -21.651      0.3956
    b_TRAIN_cost_log          -5.9103      0.1973     -29.960      0.5559
    b_SM_cost_log             -2.7788      0.1265     -21.963      0.3470
    b_CAR_cost_log            -2.1383      0.1807     -11.834      0.4447
    b_headway_generic_log     -0.8962      0.1660      -5.399      0.1801
    b_SM_seat_log             -0.1766      0.1269      -1.391      0.2022
                          Rob.t.rat.(0)
    ASC_TRAIN                    5.8007
    ASC_SM                       3.3473
    ASC_CAR                          NA
    b_time_generic_log          -8.2320
    b_TRAIN_cost_log           -10.6315
    b_SM_cost_log               -8.0082
    b_CAR_cost_log              -4.8085
    b_headway_generic_log       -4.9767
    b_SM_seat_log               -0.8734
    
    2026-07-06 08:39:58,164 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2210_3120_4120_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2210_3120_4120_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:58.202003
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -8.980217
         reciprocal of condition number         : 0.00218884
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4994.39
    Rho-squared vs equal shares                  :  0.2829 
    Adj.Rho-squared vs equal shares              :  0.2816 
    Rho-squared vs observed shares               :  0.1484 
    Adj.Rho-squared vs observed shares           :  0.1472 
    AIC                                         :  10006.78 
    BIC                                         :  10068.16 
    
    Estimated parameters                        : 9
    Time taken (hh:mm:ss)                       :  00:00:0.44 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.11 
         post-estimation                        :  00:00:0.26 
    Iterations                                  :  18  
    
    Unconstrained optimisation.
    
    Estimates:
                          Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN               1.0662     0.11851       8.997      0.2375
    ASC_SM                  0.3801     0.10181       3.734      0.1612
    ASC_CAR                 0.0000          NA          NA          NA
    b_time_generic_log     -3.2426     0.14947     -21.693      0.3908
    b_TRAIN_cost           -3.0001     0.11327     -26.486      0.3908
    b_SM_cost              -1.1039     0.05336     -20.689      0.1693
    b_CAR_cost             -0.9746     0.08985     -10.847      0.2242
    b_TRAIN_headway        -0.5172     0.10644      -4.859      0.1197
    b_SM_headway           -0.7043     0.32725      -2.152      0.2572
    b_seat_generic         -0.1208     0.08727      -1.384      0.1394
                       Rob.t.rat.(0)
    ASC_TRAIN                 4.4900
    ASC_SM                    2.3575
    ASC_CAR                       NA
    b_time_generic_log       -8.2972
    b_TRAIN_cost             -7.6760
    b_SM_cost                -6.5187
    b_CAR_cost               -4.3469
    b_TRAIN_headway          -4.3215
    b_SM_headway             -2.7388
    b_seat_generic           -0.8669
    
    2026-07-06 08:39:58,876 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2120_3210_4210_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2120_3210_4210_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:58.911941
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -26.151211
         reciprocal of condition number         : 0.00610391
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -5243.67
    Rho-squared vs equal shares                  :  0.2471 
    Adj.Rho-squared vs equal shares              :  0.246 
    Rho-squared vs observed shares               :  0.1059 
    Adj.Rho-squared vs observed shares           :  0.1049 
    AIC                                         :  10503.34 
    BIC                                         :  10557.9 
    
    Estimated parameters                        : 8
    Time taken (hh:mm:ss)                       :  00:00:0.39 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.16 
         post-estimation                        :  00:00:0.16 
    Iterations                                  :  17  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  0.4825     0.14238       3.389      0.3210
    ASC_SM                     0.5939     0.09373       6.336      0.2838
    ASC_CAR                    0.0000          NA          NA          NA
    b_TRAIN_time              -1.5234     0.07785     -19.568      0.2722
    b_SM_time                 -1.2048     0.08731     -13.800      0.4993
    b_CAR_time                -1.0401     0.06218     -16.726      0.2251
    b_cost_generic_log        -2.6564     0.11793     -22.525      0.3087
    b_headway_generic_log     -0.8692     0.15913      -5.463      0.1727
    b_SM_seat_log             -0.5460     0.12505      -4.366      0.2186
                          Rob.t.rat.(0)
    ASC_TRAIN                     1.503
    ASC_SM                        2.093
    ASC_CAR                          NA
    b_TRAIN_time                 -5.597
    b_SM_time                    -2.413
    b_CAR_time                   -4.620
    b_cost_generic_log           -8.606
    b_headway_generic_log        -5.033
    b_SM_seat_log                -2.497
    
    2026-07-06 08:39:59,385 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2220_3220_4210_5000_6220_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2220_3220_4210_5000_6220_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:39:59.449783
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -11.983007
         reciprocal of condition number         : 0.00345272
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4904.32
    Rho-squared vs equal shares                  :  0.2958 
    Adj.Rho-squared vs equal shares              :  0.2944 
    Rho-squared vs observed shares               :  0.1638 
    Adj.Rho-squared vs observed shares           :  0.1624 
    AIC                                         :  9828.65 
    BIC                                         :  9896.85 
    
    Estimated parameters                        : 10
    Time taken (hh:mm:ss)                       :  00:00:0.46 
         pre-estimation                         :  00:00:0.08 
         estimation                             :  00:00:0.1 
         post-estimation                        :  00:00:0.28 
    Iterations                                  :  14  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  1.1427      0.1979       5.774      0.4421
    ASC_SM                     0.4803      0.1286       3.735      0.2757
    ASC_CAR                    0.0000          NA          NA          NA
    b_TRAIN_time_log          -2.8184      0.2152     -13.098      0.5603
    b_SM_time_log             -3.0365      0.1801     -16.859      0.5089
    b_CAR_time_log            -3.7796      0.2099     -18.003      0.4853
    b_TRAIN_cost_log          -6.1098      0.2079     -29.394      0.6455
    b_SM_cost_log             -2.8814      0.1309     -22.008      0.3933
    b_CAR_cost_log            -1.6711      0.2232      -7.486      0.4174
    b_headway_generic_log     -0.8981      0.1657      -5.419      0.1789
    b_SM_seat_log             -0.1665      0.1273      -1.308      0.2029
                          Rob.t.rat.(0)
    ASC_TRAIN                    2.5845
    ASC_SM                       1.7419
    ASC_CAR                          NA
    b_TRAIN_time_log            -5.0305
    b_SM_time_log               -5.9667
    b_CAR_time_log              -7.7886
    b_TRAIN_cost_log            -9.4651
    b_SM_cost_log               -7.3261
    b_CAR_cost_log              -4.0034
    b_headway_generic_log       -5.0201
    b_SM_seat_log               -0.8208
    
    2026-07-06 08:40:00,000 [INFO] Delphos.apollo: Starting Apollo estimation: 1110_2120_3220_4210_5000_6110_7000
    Apollo ignition sequence completed
    Several observations per individual detected based on the value of id.
      Setting panelData in apollo_control set to TRUE.
    All checks on apollo_control completed.
    All checks on database completed.
    Model run by gnova using Apollo 0.3.7 on R 4.5.1 for Darwin.
    Please acknowledge the use of Apollo by citing Hess & Palma (2019)
      DOI 10.1016/j.jocm.2019.100170
      www.ApolloChoiceModelling.com
    
    Model name                                  : 1110_2120_3220_4210_5000_6110_7000
    Model description                           : MNL proposed by Delphos
    Model run at                                : 2026-07-06 08:40:00.074866
    Estimation method                           : bgw
    Estimation diagnosis                        : Relative function convergence (favorable)
    Optimisation diagnosis                      : Maximum found
         hessian properties                     : Negative definite
         maximum eigenvalue                     : -16.328171
         reciprocal of condition number         : 0.00309042
    Number of individuals                       : 752
    Number of rows in database                  : 6768
    Number of modelled outcomes                 : 6768
    
    Number of cores used                        :  1 
    Model without mixing
    
    LL(start)                                   : -6964.66
    LL at equal shares, LL(0)                   : -6964.66
    LL at observed shares, LL(C)                : -5865
    LL(final)                                   : -4976.16
    Rho-squared vs equal shares                  :  0.2855 
    Adj.Rho-squared vs equal shares              :  0.2841 
    Rho-squared vs observed shares               :  0.1515 
    Adj.Rho-squared vs observed shares           :  0.1502 
    AIC                                         :  9972.33 
    BIC                                         :  10040.53 
    
    Estimated parameters                        : 10
    Time taken (hh:mm:ss)                       :  00:00:0.51 
         pre-estimation                         :  00:00:0.07 
         estimation                             :  00:00:0.21 
         post-estimation                        :  00:00:0.23 
    Iterations                                  :  19  
    
    Unconstrained optimisation.
    
    Estimates:
                             Estimate        s.e.   t.rat.(0)    Rob.s.e.
    ASC_TRAIN                  1.1402     0.15765       7.232      0.3243
    ASC_SM                     0.9047     0.11106       8.146      0.2552
    ASC_CAR                    0.0000          NA          NA          NA
    b_TRAIN_time              -0.8313     0.08313     -10.001      0.2982
    b_SM_time                 -1.1078     0.08768     -12.634      0.4959
    b_CAR_time                -1.3040     0.08202     -15.899      0.2974
    b_TRAIN_cost_log          -6.0544     0.20596     -29.396      0.6367
    b_SM_cost_log             -2.8316     0.12908     -21.936      0.3899
    b_CAR_cost_log            -1.7272     0.21732      -7.948      0.5316
    b_headway_generic_log     -0.9122     0.16498      -5.529      0.1776
    b_seat_generic            -0.1346     0.08739      -1.540      0.1385
                          Rob.t.rat.(0)
    ASC_TRAIN                    3.5161
    ASC_SM                       3.5451
    ASC_CAR                          NA
    b_TRAIN_time                -2.7875
    b_SM_time                   -2.2339
    b_CAR_time                  -4.3840
    b_TRAIN_cost_log            -9.5096
    b_SM_cost_log               -7.2618
    b_CAR_cost_log              -3.2489
    b_headway_generic_log       -5.1372
    b_seat_generic              -0.9716
    
    Saved results to quick_results.csv


## 5. What to inspect first

After estimation, sort by reward or your custom score. Also inspect:

- `successfulEstimation`
- `LLout`
- `BIC`
- `nFreeParams`
- signs and magnitudes in Apollo output if saved
- repeated model families across strategies

