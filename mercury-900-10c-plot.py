
import matplotlib.pyplot as plt

for year, r_max, u_min, x, y in [(1, 4729031704.133933, 1.296079999956068e-05, [4727999464.428885, 4720263829.307716, 4697087435.3954, 4658561705.202489, 4604838614.486368, 4536130092.335845, 4452707185.196154, 4354898987.573239, 4243091343.1492047, 4117725322.8988705, 3979295484.653772, 3828347922.138613, 3665478110.31471, 3491328556.1615005, 3306586263.9411488, 3111980024.815293, 2908277541.7453156, 2696282400.8706717, 2476830901.0296483, 2250788754.8040338, 2019047673.1831644, 1782521847.835321, 1542144344.5599732, 1298863422.370001, 1053638792.7644109, 807437833.6853421, 561231773.3885498, 315991859.0409514, 72685525.34869976, -167727421.77703536, -404298591.4341948, -636094748.881389, -862201496.9072734, -1081726882.818325, -1293804916.9135454, -1497598988.4354699, -1692305165.6880832, -1877155367.1864734, -2051420391.3529592, -2214412792.8832717, -2365489594.348874, -2504054822.311576, -2629561858.200814, -2741515594.203186, -2839474386.2207284, -2923051795.9167128, -2991918114.811798, -3045801664.837587, -3084489869.595784, -3107830093.006289, -3115730241.184204, -3108159125.4864645, -3085146585.449653, -3046783370.940991, -2993220784.023436, -2924670082.141872, -2841401644.399751, -2743743905.026405, -2632082057.6098495, -2506856535.6555014, -2368561274.849714, -2217741764.722144, -2054992896.6729152, -1880956617.2593224, -1696319395.869593, -1501809516.70788, -1298194205.9266126, -1086276605.1540215, -866892603.3378274, -640907539.4743948, -409212789.1891365, -172722248.62067625, 67631270.4634394, 310899720.17916083, 556123556.0919863, 802335522.0804081, 1048564465.6198652, 1293839168.414491, 1537192177.266711, 1777663619.9653428, 2014304991.4163897, 2246182894.8899403, 2472382723.4961963, 2692012267.624435, 2904205234.1679754, 3108124663.145819, 3302966229.0358467, 3487961413.084143, 3662380534.4271307, 3825535628.056424, 3976783158.2392254, 4115526556.658491, 4241218575.3036814, 4353363444.905213, 4451518829.830025, 4535297572.948295, 4604369222.652046, 4658461335.901278, 4697360552.480216, 4720913436.5483675, 4729027081.67781], [0, 240939710.81859022, 480929129.28304356, 719021491.6125469, 954277518.8200756, 1185769122.1881628, 1412583064.5207229, 1633824562.767646, 1848620817.9562156, 2056124458.234114, 2255516881.724413, 2446011485.802134, 2626856770.1543465, 2797339301.2345066, 2956786526.719863, 3104569428.459444, 3240105003.7674394, 3362858565.257932, 3472345850.008554, 3568134929.7743807, 3649847914.5841384, 3717162443.420254, 3769812955.770293, 3807591739.0166225, 3830349747.42404, 3837997190.070335, 3830503884.819124, 3807899377.181094, 3770272823.509162, 3717772639.11074, 3650605912.511614, 3569037588.2319465, 3473389421.6381736, 3364038709.289188, 3241416800.461406, 3106007395.3974404, 2958344636.94174, 2799011003.424057, 2628635010.7610855, 2447888732.9789224, 2257485150.961532, 2058175339.96545, 1850745506.5761127, 1636013887.4528954, 1414827521.541635, 1188058908.694354, 956602567.9822325, 721371509.038137, 483293630.6017222, 243308060.30065754, 2361450.059842817, -238595758.03468478, -478613080.8877636, -716743743.6891067, -952048414.5294487, -1183598909.7397394, -1410481855.139829, -1631802288.925483, -1846687191.877252, -2054288930.9922652, -2253788603.0036945, -2444399264.514025, -2625369036.1554666, -2795984068.1297693, -2955571356.1152167, -3103501395.759488, -3239190665.5885544, -3362103928.5484548, -3471756343.049073, -3567715375.324319, -3649602505.192957, -3717094719.0994735, -3769925784.0289893, -3807887297.349593, -3830829508.5677953, -3838661909.7284813, -3831353592.3915668, -3808933369.2435107, -3771489660.3268824, -3719170143.848833, -3652181173.4635754, -3570786964.3290615, -3475308550.694919, -3366122519.4738593, -3243659524.584117, -3108402588.1620307, -2960885195.2041316, -2801689189.186295, -2631442477.0278993, -2450816552.242915, -2260523846.243659, -2061314918.199681, -1853975494.6173153, -1639323369.9993281, -1418205181.2722487, -1191493068.3187346, -960081233.9960797, -724882417.0994473, -486824292.29005355, -246845811.10716394, -5893498.529924474]), (300, 5043229057.484413, 1.2525845211385045e-05, [5042159710.521746, 5033929227.195674, 5009269267.35112, 4968277137.630507, 4911114596.057575, 4838007213.577504, 4749243483.941059, 4645173684.943545, 4526208495.964622, 4392817377.090841, 4245526716.28478, 4084917751.965595, 3911624279.415519, 3726330149.2921495, 3529766568.824631, 3322709216.2155914, 3105975179.5188804, 2880419732.197679, 2646932957.8536305, 2406436237.4617605, 2159878613.555144, 1908233045.0372937, 1652492567.5021195, 1393666374.5728366, 1132775835.3654153, 870850464.0455004, 608923857.1411892, 348029614.79656166, 89197262.0862751, -166551813.55929738, -418208392.82738096, -664779406.9509312, -905291856.3264289, -1138796649.9824452, -1364372350.6476033, -1581128810.6099124, -1788210684.213201, -1984800802.844848, -2170123399.4089785, -2343447169.2838597, -2504088156.0040417, -2651412449.7078147, -2784838688.6570644, -2903840352.846588, -3007947841.648733, -3096750326.458257, -3169897371.7617593, -3227100317.79119, -3268133419.323244, -3292834736.346346, -3301106772.9099545, -3292916861.7128444, -3268297292.7958727, -3227345186.108341, -3170222107.853099, -3097153433.1402574, -3008427456.4392343, -2904394253.8105187, -2785464301.3340654, -2652106855.2091737, -2504848100.1033797, -2344269072.755827, -2171003368.8893905, -1985734643.1504364, -1789193911.3216822, -1582156665.5870545, -1365439814.5136786, -1139898459.5199907, -906422520.6441863, -665933224.9635566, -419379471.5429826, -167734087.20026115, 88010012.13079062, 346843739.2626302, 607745817.3906327, 869686809.7994528, 1131633181.7453604, 1392551378.5307558, 1651411903.504363, 1907193380.1216707, 2158886581.958398, 2405498414.70464, 2646055834.468754, 2879609687.0043364, 3105238452.704762, 3322051882.3830113, 3529194509.78982, 3725849026.818844, 3911239508.1822295, 4084634472.6844935, 4245349769.263825, 4392751276.288064, 4526257403.212536, 4645341385.416993, 4749533362.02204, 4838422229.926439, 4911657265.711057, 4968949508.892794, 5010072902.221381, 5034865183.330862, 5043228524.833843], [-14313.375654914002, 256138438.81822726, 511280595.3151747, 764405286.8607676, 1014513606.6301554, 1260618552.1629066, 1501748920.359377, 1736953140.0628808, 1965303027.1705205, 2185897447.385113, 2397865872.285107, 2600371814.71609, 2792616129.5126877, 2973840167.0904307, 3143328766.9993997, 3300413080.1734753, 3444473208.098767, 3574940649.025976, 3691300541.1459317, 3793093694.2536006, 3879918401.5640163, 3951432024.7321076, 4007352345.8351545, 4047458680.800573, 4071592749.9756274, 4079659302.51381, 4071626492.157911, 4047526002.6241736, 4007452922.2912784, 3951565368.816837, 3880083864.877063, 3793290467.8024087, 3691527656.269787, 3575196978.833139, 3444757468.818143, 3300723832.987864, 3143664420.3758397, 2974198979.078585, 2792996210.963376, 2600771132.567278, 2398282253.4749117, 2186328583.2260203, 1965746478.4483106, 1737406342.4168367, 1502209190.3815615, 1261083094.2066278, 1014979520.2179953, 764869574.7024487, 511740171.9688585, 256590140.1166202, 426279.653527279, -255740609.24501458, -510899715.25570905, -764044204.5099002, -1014175193.4104184, -1260305690.1481814, -1501464489.2289464, -1736700003.7169378, -1965084020.0878375, -2185715360.8554997, -2397723440.415115, -2600271700.0076284, -2792560908.6797605, -2973832316.9524436, -3143370650.54025, -3300506932.5838084, -3444621123.155012, -3575144565.486033, -3691562229.852114, -3793414745.388566, -3880300212.609133, -3951875789.0091085, -4007859041.3975964, -4048029060.2244368, -4072227331.008564, -4080358359.562067, -4072390048.5618715, -4048353823.947242, -4008344510.688574, -3952519958.3246512, -3881100418.0795827, -3794367673.557414, -3692663928.7400317, -3576390457.529822, -3446006020.1678505, -3302025053.2872133, -3145015639.6258783, -2975597266.598341, -2794438381.8452888, -2602253755.774214, -2399801661.0933266, -2187880881.0671115, -1967327557.4220386, -1739011891.5364473, -1503834710.8260944, -1262723914.3092227, -1016630811.4739987, -766526368.9104351, -513397379.16680163, -258242567.351325, -2068650.6075967567]), (600, 5369668067.464369, 1.2115397090266849e-05, [5368561185.916766, 5359819679.203291, 5333629289.602064, 5290093365.854637, 5229383709.188924, 5151739895.103358, 5057468327.740753, 4946941030.477751, 4820594177.735419, 4678926373.360901, 4522496682.990153, 4351922427.258463, 4167876745.662426, 3971085940.004389, 3762326608.0261345, 3542422578.322916, 3312241659.3622236, 3072692214.5257564, 2824719577.371243, 2569302320.9214177, 2307448395.8434963, 2040191152.6670036, 1768585263.7217503, 1493702561.10965, 1216627806.8316274, 938454412.0805552, 660280122.2847719, 383202685.1025213, 108315518.50648127, -163296604.08627218, -430561834.5458208, -692425479.6902647, -947854163.2337707, -1195839903.5640328, -1435404091.3499184, -1665601351.1497788, -1885523271.8676913, -2094301991.2891984, -2291113620.6428943, -2475181495.590262, -2645779240.920268, -2802233636.556801, -2943927273.9789987, -3070300992.7130437, -3180856086.2889123, -3275156270.084394, -3352829402.710437, -3413568954.3713684, -3457135216.467683, -3483356247.1260643, -3492128549.510499, -3483417480.254623, -3457257385.871736, -3413751467.1628222, -3353071371.7636023, -3275456516.6657615, -3181213143.4821177, -3070713109.6330066, -2944392420.9451814, -2802749511.037897, -2646343274.188541, -2475790859.834, -2291765237.1968594, -2094992539.5783176, -1886249198.7197483, -1666358881.0048478, -1436189237.2078085, -1196648478.4752774, -948681792.4576716, -693267613.6811264, -431413762.5197207, -164153468.35883012, 107458707.48672189, 382351033.01630974, 659438834.5033466, 937628776.4954257, 1215823175.977869, 1492924333.5879931, 1767838864.9775872, 2039482015.0045545, 2306781937.9944696, 2568683926.953387, 2824154575.1442733, 3072185853.471233, 3311799087.9064593, 3542048821.042443, 3762026542.5229335, 3970864273.6549606, 4167737992.0014677, 4351870882.732461, 4522536403.584676, 4679061151.128221, 4820827518.0167, 4947276129.640807, 5057908050.928688, 5152286755.023881, 5230039845.700906, 5290860526.10753, 5334508809.289954, 5360812464.9303055, 5369667698.70709], [-16246.860908742136, 271841426.08922666, 542626489.2838266, 811270312.1698066, 1076712715.3015325, 1337906154.2326384, 1593819853.5887053, 1843443874.7418826, 2085793101.4235861, 2319911127.3305297, 2544874030.3575215, 2759794018.7149386, 2963822934.1436725, 3156155599.2319016, 3336032994.6686563, 3502745254.5283737, 3655634467.434977, 3794097272.764106, 3917587241.482433, 4025617032.448936, 4117760315.415421, 4193653453.186106, 4252996936.5363197, 4295556565.95201, 4321164375.339934, 4329719295.205016, 4321187550.713463, 4295602795.01874, 4253065976.056481, 4193744938.1553807, 4117873759.2641435, 4025751827.133187, 3917742657.499384, 3794272459.4910808, 3655828453.4390016, 3502956948.0604815, 3336261184.2966557, 3156398954.883407, 2964080008.2260227, 2760063247.6603613, 2545153736.6176996, 2320199521.391454, 2086088284.8166158, 1843743843.2837596, 1594122501.094267, 1338209276.877541, 1077014016.5617416, 811567408.4762994, 542916916.1128703, 272122644.8164323, 253158.50765153574, -271618736.88193125, -542420226.7504675, -811082721.1531917, -1076546071.5173244, -1337762753.9649363, -1593702002.8771544, -1843353878.265991, -2085733250.9760368, -2319883690.020065, -2544881236.5258303, -2759838049.411737, -2963905909.0434737, -3156279564.2077374, -3336199909.1666856, -3502956979.0601068, -3655892751.2058406, -3794403741.5031285, -3917943385.481608, -4026024194.8474092, -4118219680.9336724, -4194166037.201398, -4253563574.677772, -4296177904.18462, -4321840860.8654375, -4330451167.7101145, -4321974834.714132, -4296445293.012197, -4253963262.6445746, -4194696354.6546693, -4118878409.8306537, -4026808575.5855017, -3918850125.548847, -3795429025.853997, -3657032254.2190285, -3504205878.248932, -3337552900.6493006, -3157730879.7487707, -2965449334.8168583, -2761466946.273909, -2546588562.1352067, -2321662022.2049737, -2087574812.492047, -1845250563.4396737, -1595645405.5203125, -1339744196.5528083, -1078556635.6026714, -813113279.0707728, -544461474.4382238, -273661227.69044405, -1781020.8965011365]), (900, 5707406450.398224, 1.172872782018497e-05, [5706261804.434498, 5696996517.479036, 5669232246.305838, 5623078544.933513, 5558717535.722046, 5476403190.08655, 5376460326.491435, 5259283328.41181, 5125334587.861022, 4975142680.600173, 4809300279.836443, 4628461817.508988, 4433340901.430455, 4224707499.499845, 4003384900.7392187, 3770246466.6660905, 3526212184.565007, 3272245037.1009755, 3009347201.955635, 2738556097.1786647, 2460940287.314933, 2177595266.5701146, 1889639135.8315687, 1598208190.452157, 1304452436.3789346, 1009531052.1498387, 714607814.58003, 420846506.45752627, 129406324.2646039, -158562696.05043918, -441924217.0532042, -719560083.7652017, -990374735.8203745, -1253299530.4401572, -1507296959.1190906, -1751364741.47766, -1984539780.08406, -2205901960.6297, -2414577782.356491, -2609743804.838617, -2790629896.909674, -2956522275.228573, -3106766320.751601, -3240769161.586591, -3358002012.1029797, -3458002259.3538566, -3540375288.263872, -3604796038.563582, -3651010287.200894, -3678835651.4264054, -3688162308.246684, -3678953427.620871, -3651245317.600745, -3605147280.8802757, -3540841183.4549823, -3458580736.8978214, -3358690496.918011, -3241564582.600814, -3107665121.257262, -2957520424.776638, -2791722904.6213136, -2610926734.324111, -2415845267.9230676, -2207248225.1814957, -1985958654.169243, -1752849683.602897, -1508841077.383988, -1254895605.4391594, -992015244.6751279, -721237225.3128151, -443629938.16306627, -160288718.96649194, 127668473.54472569, 419105468.8261571, 712872367.5195733, 1007810078.617919, 1302754892.837213, 1596543074.1903138, 1888015451.6242719, 2176021992.644415, 2459426340.8515625, 2737110299.4678125, 3007978243.227998, 3270961441.101422, 3525022273.0252, 3769158323.892041, 4002406338.2263665, 4223846020.9352093, 4432603668.009233, 4627855613.527888, 4808831479.958119, 4974817216.747651, 5125157917.852968, 5259260405.325642, 5376595569.934618, 5476700458.11739, 5559180098.76225, 5623709060.858161, 5670032737.843852, 5697968351.751554, 5707405674.291122], [-59818.05073850858, 287970040.0405538, 574863680.0809568, 859488960.6734788, 1140722692.733666, 1417455071.8516738, 1688594057.6845753, 1953069683.3909552, 2209838277.8452106, 2457886584.0898013, 2696235757.5962987, 2923945228.9135604, 3140116415.2853866, 3343896266.370585, 3534480630.580988, 3711117428.0061555, 3873109618.1763916, 4019817950.3924975, 4150663486.3291993, 4265129884.3362017, 4362765436.596467, 4443184851.66592, 4506070774.726984, 4551175039.266339, 4578319646.344242, 4587397466.912085, 4578372664.259381, 4551280834.949468, 4506228868.359832, 4443394524.393991, 4363025731.925894, 4265439610.0896, 4151021217.4118667, 4020222031.2549567, 3873558166.3170443, 3711608338.0111723, 3535011578.5768466, 3344464715.4101973, 3140719620.992081, 2924580246.0824113, 2696899447.3466496, 2458575621.7482295, 2210549161.6579623, 1953798744.1248574, 1689337468.714306, 1418208860.2144437, 1141482750.9354212, 860251059.2471248, 575623481.0094813, 288723110.8504767, 682010.6362200087, -287363257.481048, -574276115.7496189, -858924455.5702606, -1140185104.5632985, -1416948258.4125192, -1688121859.931087, -1952635908.1400106, -2209446680.247379, -2457540849.800806, -2695939485.237939, -2923701912.2311883, -3139929425.4183636, -3343768834.5008287, -3534415830.3018293, -3711118158.626139, -3873178587.8912096, -4019957660.335741, -4150876214.9191675, -4265417672.2449574, -4363130072.644487, -4443627859.30051, -4506593399.15798, -4551778235.840873, -4579004070.216578, -4588163463.36539, -4579220260.104847, -4552209731.590432, -4507238435.885253, -4444483797.155944, -4364193405.508923, -4266684039.843387, -4152340417.666347, -4021613677.1783714, -3875019597.0059686, -3713136560.789761, -3536603275.230333, -3346116249.572696, -3142427047.6108685, -2926339322.0335364, -2698705643.477885, -2460424136.636193, -2212434936.6784782, -1955716479.7035246, -1691281642.2843857, -1420173744.978315, -1143462435.9871283, -862239470.7087961, -577614404.2637969, -290710213.72099006, -2658867.4266923964])]:
    plt.plot(x, y, label=f'{year}, {r_max / 4727999464.428885:.4g}, {u_min / 1.2962300739400189e-05:.3g}')
plt.title("""Retarded interaction - Sun-Mercury - 10c
Changes of orbit after many orbital period
u[0] = 1.296e-05  r%[0] = 4.728e+09""")
plt.legend(title='period, r_max / r[0], u_min / u[0]')
plt.xlabel('r_x%')
plt.ylabel('r_y%')
plt.show()