def Breakpoint(p):
  p = p.strip("()")
  p = p.strip("\n")
  p = p.split(" ")
  p1=[]
  counter = 0
  for br in p:
    p1.append(int(br))
  produzeni_p=[0]+p1+[len(p1)+1]
  for i in range(len(p1)):
    if(produzeni_p[i+1] != produzeni_p[i] + 1):
      counter += 1

  return counter

print(Breakpoint("""(+1 +2 +3 +4 +5 +6 +7 +8 +9 +10 +11 +12 +13 +14 +15 +16 +17 +18 +19 +20 +21 +22 +23 +24 +25 +26 +27 +28 +29 +30 +31 +32 +33 +34 +35 +36 +37 +38 +39 +40 +41 +42 +43 +44 +45 +46 +47 +48 +49 +50 +51 +52 +53 +54 +55 +56 +57 +58 +59 +60 +61 +62 +63 +64 +65 +66 +67 +68 +69 +70 +71 +72 +73 +74 +75 +76 +77 +78 +79 +80 +81 +82 +83 +84 +85 +86 +87 +88 +89 +90 +91 +92 +93 +94 +95 +96 +97 +98 +99 +100 +101 +102 +103 +104 +105 +106 +107 +108 +109 +110 +111 +112 +113 +114 +115 +3679 +3680 +3681 +3682 +3683 +3684 +3685 +3686 +3687 +3688 +3689 +3690 +3691 +931 +932 +933 +934 +935 +936 +937 +938 +939 +940 +941 +942 +943 +944 +945 +946 +947 +948 +949 +950 +951 +952 +953 +954 +955 +956 +957 +958 +959 +960 +961 +962 +963 +964 +965 +966 +967 +968 +969 +970 +971 +972 +973 +974 +975 +976 +977 +978 +979 +980 +981 +982 +983 +984 +985 +986 +987 +988 +989 +990 +991 +992 +993 +994 +995 +996 +997 +998 +999 +1000 +1001 +1002 +1003 +1004 +1005 +1006 +1007 +1008 +1009 +1010 +1011 +1012 +1013 +1014 +1015 +1016 +1017 +1018 +1019 +1020 +1021 +1022 +1023 +1024 +1025 +1026 +1027 +1028 +1029 +1030 -222 -221 -220 -219 -218 -217 -216 -215 -214 -213 -212 -211 -210 -209 -208 -207 -206 -205 -204 -203 -202 -201 -200 -199 -198 -197 -196 -195 -194 -193 -192 -191 -190 -189 -188 -187 -186 -185 -184 -183 -182 -181 -180 -179 -178 -177 -176 -175 -174 -173 -172 -171 -170 -169 -168 -167 -166 -165 -164 -163 -162 -161 -160 +716 +717 +718 +719 +720 +721 +722 +723 +724 +725 +726 +727 +728 +729 +730 +731 +732 +733 +734 +735 +736 +737 +738 +739 +740 +741 +742 +743 +744 +745 +746 +747 +748 +749 +750 +751 +752 +753 +754 +755 +756 +757 +758 +759 +760 +761 +762 +763 +764 +765 +766 +767 +768 +769 +770 +771 +772 +773 +774 +775 +776 +777 +778 +779 +780 +781 +782 +783 +784 +785 +786 +787 +788 +789 +790 +791 +792 +793 +794 +795 +796 +797 +798 +799 +800 +801 +802 +803 +804 +805 +806 +807 +808 +809 +810 +811 +812 +813 +814 -553 -552 -551 -550 -549 -548 -547 -546 -545 -544 -543 -542 -1682 -1681 -1680 -1679 -1678 -1677 -1676 -1675 -1674 -1673 -1672 -1671 -1670 +1771 +1772 +1773 +1774 +1775 +1776 +1777 +1778 +1779 +1780 +1781 +1782 +1783 +1784 +1785 +1786 +1787 +1788 +1789 +1790 +1791 +1792 +1793 +1794 +1795 +1796 +1797 +1798 +1799 +1800 +1801 +1802 +1803 +3921 +2568 +2569 +2570 +2571 +2572 +2573 +2574 +2575 +2576 +2577 +2578 +2579 +2580 +2581 +2582 +2583 +2584 +2585 +2586 +2587 +2588 +2589 +2590 +2591 +2592 +2593 +2594 +2595 +2596 +2597 +2598 +2599 +2600 +2601 +2602 +2603 +2604 +2605 +2606 +2607 +2608 +2609 +2610 +2611 +2612 +2613 +2614 +2615 +2616 +2617 +2618 +2619 +2620 +2621 +2622 +2623 +2624 +2625 +2626 +2627 +2628 +2629 +2630 +2631 +2632 +2633 +2634 +2635 +2636 +2637 +2638 +2639 +2640 +2641 +2642 +2643 +2644 +2645 +2646 +2647 +2648 +2649 +2650 +2651 +2652 +2653 +2654 +2655 +2656 +2657 +2658 +2659 +2660 +2661 +2662 +2663 +2664 +2665 +2666 +2667 +2668 +2669 +2670 +2671 +2672 +2673 +2674 +2675 +2676 +2677 +2678 +2679 -2449 -2448 -2447 +3539 +3540 +3541 +3542 +3543 +3544 +3545 +3546 +3547 +3548 +3549 +3550 +3551 +3552 +3553 +3554 +3555 +3556 +3557 +3558 +3559 +3560 +3561 +3562 +3563 +3564 +3565 +3566 +3567 +3568 +3569 +3570 +3571 +3572 +3573 +3574 +3575 +3576 +3577 +3578 +3579 +3580 +3581 +3582 +3583 +3584 +3585 +3586 +3587 +3588 +3589 +3590 +3591 +3592 +3593 +3594 +3595 +3596 +3597 +3598 +3599 +3600 +3601 +3602 +3603 +3604 +3605 +3606 +3607 +3608 +3609 +3610 +3611 +3612 +3613 +3614 +3615 +3616 +3617 +3618 +3619 +3620 +3621 +3622 +3623 +3624 +3625 +3626 +3627 +3628 +3629 +3630 +3631 +3632 +3633 +3634 +3635 +3636 +3637 +3638 +3639 +3640 +3641 +3642 +3643 +3644 +3645 +3646 +3647 +3648 +3649 +3650 +3651 +3652 +3653 +3654 +3655 +3656 +3657 +3658 +3659 +3660 +3661 +3662 +3663 +3664 +3665 +3666 +3667 +3668 -476 -475 -474 -473 +861 +862 +863 +864 +524 +525 +526 +527 +528 +529 +530 +531 +532 +533 +534 +535 +536 +537 +538 +539 +540 +541 +1683 +1684 +1685 +1686 +1687 +1688 +1689 +1690 +1691 +1692 +1693 +1694 +1695 +1696 +1697 +1698 +1699 +1700 +1701 +1702 +1703 +1704 +1705 +1706 +1707 +1708 +1709 +1710 +1711 +1712 +1713 +1714 +1715 +1716 +1717 +1718 +1719 +1720 +1721 +1722 +1723 +1724 +1725 +1726 +1727 +1728 +1729 +1730 +1731 +1732 +1733 +1734 +1735 +1736 +1737 +1738 +1739 +1740 +1741 +1742 +1743 +1744 +1745 +1746 +1747 +1748 +1749 +1750 +1751 +1752 +1753 +3959 +3960 +3961 +3962 +3963 +3964 +3965 +3966 +3967 +3968 +3969 +3970 +3971 +3972 +3973 -3895 -3894 -3893 -3892 -3891 -3890 -3889 -3888 -3887 -3886 -3885 -3884 -3883 -3882 -3881 -3880 -3879 -3878 -3877 -3876 -3875 -3874 -3873 -3872 -3871 -3870 -3869 -3868 -3867 -3866 -3865 -3864 -3863 -3862 -3861 -3860 -3859 -3858 -3857 -3856 -3855 -3854 -3853 -3852 -3851 -3850 -3849 -3848 -3847 -3846 -3845 -3844 -3843 -3842 -3841 -3840 -3839 -3838 -3837 -3836 -3835 -3834 -3833 -3832 -3831 -3830 -3829 -3828 -3827 -3826 -3825 -3824 -3823 -3822 -3821 -3820 -3819 -3818 -3817 -3816 -3815 -3814 -3813 -3812 -3811 -3810 -3809 -3808 -3807 -3806 -3805 -3804 -3803 -3802 -2484 -2483 -2482 -2481 -2480 -2479 -2478 -2477 -2476 -2475 -2474 -2473 -2472 -2471 -2470 -2469 -2468 -2467 -2466 -2465 -2464 -2463 -2462 -2461 -2460 -2459 -2458 -2457 -2456 -2455 -2454 -2453 -2452 -2451 -2450 +2680 +2681 +2682 +2683 +2684 +2685 +2686 +2687 +2688 +2689 +2690 +2691 +2692 +2693 +2694 +2695 +2696 +2697 +2698 +2699 +2700 +2701 +2702 +2703 +2704 +2705 +2706 +2707 +2708 +2709 +2710 +2711 +2712 +2713 +2714 +2502 +2503 +2504 +2505 +1281 +1282 +1283 +1284 +1285 +1286 +1287 +1288 +1289 +1290 +1291 +1292 +1293 +1294 +1295 +1296 +1297 +1298 +1299 +1300 +1301 +1302 +1303 +1304 +1305 +1306 +1307 +1308 +1309 +1310 +1311 +1312 +1313 +1314 +1315 +1316 +1317 +1318 +1319 +1320 +1321 +1322 +1323 +1324 +1325 +1326 +1327 +1328 +1329 +1330 +1331 +1332 +1333 +1334 +1335 +1336 +1337 +1338 +1339 +1340 +1341 +1342 +1343 +1344 +1345 +1346 +1347 +1348 +1349 +1350 +1351 +1352 +1353 +1354 +1355 +1356 +1357 +1358 +1359 +1360 +1361 +1362 +1363 +1364 +1365 +1366 +1367 +1368 +1369 +1370 +1371 +1372 +1373 +1374 +1375 +1376 +1377 +1378 +1379 +1380 +1381 +1382 +1383 +1384 +1385 +1386 +1387 +1388 +1389 +1390 +1391 +1392 +1393 +1394 +1395 +1396 +1397 +1398 +1399 +1400 +1401 +1402 +1403 +1404 +1405 +1406 +1407 +1408 +1409 +1410 -3448 -3447 -3446 -3445 -3444 -3443 -3442 -3441 -3440 -3439 -3438 -3437 -3436 -3435 -3434 -3433 -3432 -3431 -3430 -3429 -3428 -3427 -3426 -3425 -3424 -3423 -3422 -3421 -3420 -3419 -3418 -3417 -3416 -3415 -3414 -3413 -3412 -3411 -3410 -3409 -3408 -3407 -3343 -3342 -3341 -3340 -3339 -3338 -3337 -3336 -3335 -3334 -3333 -3332 -3331 -3330 -3329 -3328 -3327 -3326 -3325 -3324 -3323 -3322 -3321 -3320 -3319 -3318 -3317 -3316 -3315 -3314 -3313 -3312 -3311 -3310 -2120 -2119 -2118 -2117 -2116 -2115 -2114 -2113 -2112 -2111 -2110 -2109 -2108 -2107 -2106 -2105 -2104 -2103 -2102 -2101 -2100 -2099 -2098 -2097 -2096 -2095 -2094 -2093 -2092 -2091 -2090 -2089 -2088 -2087 -2086 -2085 -2084 -2083 -2082 -2081 -2080 -2079 -2078 -2077 -2076 -2075 -2074 -2073 -2072 -2071 -2070 -2069 -2068 -2067 -2066 -2065 -2064 -2063 -2062 -2061 -2060 -2059 -2058 -2057 -2056 -2055 -2054 -2053 -2052 -2051 -2050 -2049 -2431 -2430 -2429 -2428 -2427 -2426 -2425 -2424 -2423 -2422 -2421 -2420 -2419 -2418 -2417 -2416 -2415 -2414 -2413 -2412 -2411 -2410 -2409 -2408 -2407 -2406 -2405 -2404 -2403 -2402 -2401 -2400 -2399 -2398 -2397 -2396 -2395 -2394 -2393 -2392 -2391 -2390 -2389 -2388 -2387 -2386 -2385 -2384 -2383 -2382 -2381 -2380 -2379 -2378 -2377 -2376 -2375 -2374 -2373 -2372 -2371 -2370 -2369 -2368 -2367 -2366 -2365 -2364 -2363 -2362 -2361 -2360 -2359 -2358 -2357 -2356 -2355 -2354 -2353 -2352 -2351 -2350 -2349 -2348 -2347 -2346 -2345 -2344 -2343 -2342 -2341 -2340 -2339 -2338 -2337 -2336 -2335 -2334 -2333 -2332 -2331 -2330 -2329 -2328 -2327 -2326 -2325 -2324 -2323 -2322 -2321 -2320 -2319 -2318 -2317 -2316 -2315 -2314 -2313 -2312 -2311 -2310 -2309 -2308 -2307 -2306 -2305 -2304 -2303 -2302 -2301 -2300 -2299 -2298 -2297 -2296 -2295 -2294 -2293 -2292 -2291 -2290 -2289 -2288 -2287 -2286 -2285 -2284 -2283 -2282 -2281 -2280 -2279 -2278 -2277 -2276 -2275 -2274 -2273 -2272 -2271 -2270 -2269 -2268 -2267 -2266 -2265 -2264 -2263 -2262 -2261 -2260 -2259 -2258 -2257 -2256 -2255 -2254 -2253 -2252 -2251 -2250 -2249 -2248 -2247 -2246 -2245 -2244 -2243 -2242 -2241 -2240 -2239 -2238 -2237 -2236 -2235 -2234 -2233 -2232 -2231 -2230 -2229 -2228 -2227 -2226 -2225 -2224 -2223 -2222 -2221 -2220 -2219 -2218 -2217 -2216 -2215 -2214 -2213 -2212 -2211 -2210 -2209 -2208 -2207 -2206 -2205 -2204 -2203 -2202 -2201 -2200 -2199 -2198 -2197 -2196 -2195 -2194 -2193 -2192 -2191 -641 -640 -639 -638 -637 -636 -635 -634 -633 -632 -631 +1441 +1442 +1443 +1444 +1445 +1446 +1447 +1448 +1449 +1450 +1451 +1452 +1453 +1454 +1455 +1456 +1457 +1458 +1459 +1460 +1461 +1462 +1463 +1464 +1465 +1466 +1467 +1468 +1469 +1470 +1471 +1472 +1473 +1474 +1475 +1476 +1477 +1478 +1479 +1480 +1481 +1482 +1483 +1484 +1485 +1486 +1487 +1488 +1489 +1490 +1491 +1492 +1493 +1494 +1495 +1496 +1497 +1498 +1499 +1500 +1501 +1502 +1503 +1504 +1505 +1506 +1507 +1508 +1509 +1510 +1511 +1512 +1513 +1514 +1515 +1516 +1517 +1518 +1519 +1520 +1521 +1522 +1523 +1524 +1525 +1526 +1527 +1528 +1529 +1530 +1531 +1532 +1533 +1534 +1535 +1536 +1537 +1538 +1539 +1540 +1541 +1542 +1543 +1544 +1545 +1546 +1547 +1548 +1549 +1550 +1551 +1552 +1553 +1554 +1555 +1556 +1557 +1558 +1559 +1560 +1561 +1562 +1563 +1564 +1565 +1566 +1567 +1568 +1569 +1570 +1571 +1572 +1573 +1574 +1575 +1576 +1577 +1578 +1579 +1580 +1581 +1582 +1583 +1584 +1585 +1586 +1587 +1588 +1589 +1590 +1591 +1592 +1593 +1594 +1595 +1596 +1597 +1598 +1599 +1600 +1601 +1602 +1603 +1604 +1605 +1606 +1607 +1608 +1609 +1610 +1611 +1612 +1613 +1614 +1615 +1616 +1617 +1618 +1619 +1620 +1621 +1622 +1623 +1624 +1625 +1626 +1627 +1628 +1629 +1630 +1631 +1632 +1633 +1634 +1635 +1636 +1637 +1638 +1639 +1640 +1641 +1642 +1643 +1644 +1645 +1646 +1647 +1648 +1649 +1650 +1651 +1652 +1653 +1654 +3705 +3706 +3707 +3708 +3709 +3710 +3711 -3003 -3002 -3001 -3000 -2999 -2998 -2997 -2996 -2995 -2994 -2993 -2992 -2991 -2990 -2989 -2988 -2987 -2986 -2985 -2984 -2983 -2982 -2981 -2980 -2979 -2978 -2977 -2976 -2975 -2974 -2973 -2972 -2971 -2970 -2969 -2968 -2967 -2966 -2965 -2964 -2963 -2962 -2961 -2960 -2959 -2958 -2957 -2956 -2955 -2954 -2953 -2952 -710 -709 -708 -707 -706 -705 -704 -703 -702 -701 -700 -699 -698 -697 -696 -695 -694 -693 -692 -691 -690 -689 -688 -687 -686 -685 -684 -683 -682 -681 -680 -679 -678 -677 -676 -675 -674 -673 -672 -671 -670 -669 -668 -667 -666 -665 -664 -663 -662 -661 -660 -659 -658 -657 -656 -655 -654 -653 -652 -651 -650 -649 -648 -647 -646 -645 -644 -643 -642 -2190 -2189 -2188 -2187 -2186 -2185 -2184 -2183 -2182 -2181 -2180 -2179 -2178 -2177 -2176 -2175 -2174 -2173 -2172 -2171 -2170 -2169 -2168 -2167 -2166 -2165 -2164 -2163 -2162 -2161 -2160 -2159 -2158 -2157 -2156 -2155 -2154 -2153 -2152 -2151 -2150 -2149 -2148 -2147 -2146 -2145 -2144 -2143 -2142 -2141 -2140 -2139 -2138 -2137 -2136 -2135 -2134 -2133 -2132 -2131 -2130 -2129 -2128 -2127 -2126 -2125 -2124 -2123 -2122 -2121 -3309 -3308 -3307 -3306 -3305 -3304 -3303 -3302 -3301 -3300 -3299 -3298 -3297 -3296 -3295 -3294 -3293 -3292 -3291 -3290 -3289 -3288 -3287 -3286 -3285 -3284 -3283 -3282 -3281 -3280 -3279 -3278 -3277 -3276 -3275 -3274 -3273 -3272 -3271 -3270 -3269 -3268 -3267 -3266 -3265 -3264 -3263 -3262 -3261 -3260 -3259 -3258 -3257 -3256 -3255 -3254 -3253 -3252 -3251 -3250 -3249 -3248 -3247 -3246 -3245 -3244 -3243 -3242 -3241 -3240 -3239 -3238 -3237 -3236 -3235 -3234 -3233 -3232 -3231 -3230 -3229 -3228 -3227 -3226 -3225 -3224 -3223 -3222 -3221 -3220 -3219 -3218 -3217 -3216 -3215 -3214 -1125 -1124 -1123 -1122 -1121 -1120 -1119 -1118 -1117 -1116 -1115 -1114 -1113 -1112 -1111 -1110 -1109 -1108 -1107 -1106 -1105 -1104 -1103 -1102 -1101 -1100 -1099 -1098 -1097 -1096 -1095 -1094 -1093 -1092 -1091 -1090 -1089 -1088 -1087 -1086 -1085 -1084 -1083 -1082 -1081 -1080 -1079 -1078 -1077 -1076 -1075 -1074 -1073 -1072 -1071 -1070 -1069 -1068 -1067 -1066 -1065 -1064 -1063 -1062 -1061 -1060 -1059 -1058 -1057 -1056 -1055 -1054 -1053 -1052 -1051 -1050 -1049 -1048 -1047 -1046 -1045 -1044 -1043 -1042 -1041 -1040 -1039 -1038 -1037 -1036 -1035 -1034 -1033 -1032 -1031 +223 +224 +225 +226 +227 +228 +229 +230 +231 +232 +233 +234 +235 +236 +237 +238 +239 +240 +241 +242 +243 +244 +245 +246 +247 +248 +249 +250 +251 +252 +253 +254 +255 +256 +257 +258 +259 +260 +261 +262 +263 +264 +265 +266 +267 +268 +269 +270 +271 +272 +273 +274 +275 +276 +277 +278 +279 +280 +281 +282 +283 +284 +285 +286 +287 +288 +289 +290 +291 +292 +370 +371 +372 +373 +374 +375 +376 +377 +378 +379 +380 +381 +382 +383 +384 +385 +386 +387 +388 +389 +390 +391 +392 +393 +394 +395 +396 +3452 +3453 +3454 +3455 +3456 +3457 +3458 +3459 +3460 +3461 +3462 +3463 +3464 +3465 +3466 +3467 +3468 +3469 +3470 +3471 +3472 +3473 +3474 +3475 +3476 +3477 +3478 +3479 +3480 +3481 +3482 +3483 +3484 +3485 +3486 +3487 +3488 +3489 +3490 +3491 +3492 +3493 +3494 +3495 +3496 +3497 +3498 +3499 +3500 +3501 +3502 +3503 +3504 +3505 +3506 +3507 +3508 +3509 +3510 +3511 +3512 +3513 +3514 +3515 +3516 +3517 +3518 +3519 +3520 +3521 +453 +454 +455 +456 +457 +458 +459 +460 +461 +462 +463 +464 +465 +466 +467 +468 +469 +470 +471 +472 -860 -859 -858 -857 -856 -855 -854 -853 -852 -851 -850 -849 -848 -847 -846 -845 -844 -843 -842 -841 -840 -839 -838 -837 -836 -835 -834 -833 -832 -831 -830 -829 -828 -827 -826 -825 -824 -823 -822 -821 -820 -819 -818 -817 -816 -815 +554 +555 +556 +557 +558 +559 +560 +561 +562 +563 +564 +565 +566 +567 +568 +569 +570 +571 +572 +573 +574 +575 +576 +577 +578 +579 +580 +581 +582 +583 +584 +585 +586 +587 +588 +589 +590 +591 +592 +593 +594 +595 +596 +597 +598 +599 +600 +601 +602 +603 +604 +605 +606 +607 +608 +609 +610 +611 +612 +613 +614 +615 +616 +617 +618 +619 +620 +621 +622 +623 +624 +625 +626 +627 +628 +629 +630 -1440 -1439 -1438 -1437 -1436 -1435 -1434 -1433 -1432 -1431 -1430 -1429 -1428 -1427 -1426 -1425 -1424 -1155 -1154 -1153 -1152 -1151 -1150 -1149 -1148 -1147 -1146 -1145 -1144 -1143 -1142 -1141 -1140 -1139 -1138 -1137 -1136 -1135 -1134 -1133 -1132 -1131 -1130 -1129 -1128 -1127 -1126 -3213 -3212 -3211 -3210 -3209 -3208 -3207 -3206 -3205 -3204 -3203 -3202 -3201 -3200 -3199 -3198 -3197 -3196 -3195 -3194 -3193 -3192 -3191 -3190 -3189 -3188 -3187 -3186 -3185 -3184 -3183 -3182 -3181 -3180 -3179 -3178 -3177 -3176 -3175 -3174 -3173 -3172 -3171 -3170 -3169 -3168 -3167 -3166 -3165 -3164 -3163 -3162 -3161 -3160 -3159 -3158 -3157 -3156 -3155 -3154 -3153 -3152 -3151 -3150 -3149 -3148 -3147 -3146 -3145 -3144 -3143 -3142 -3141 -3140 -3139 -3138 -3137 -3136 -3135 -3134 -3133 -3132 -3131 -3130 -3129 -3128 -3127 -3126 -3125 -3124 -3123 -3122 -3121 -3120 -3119 -3118 -3117 -3116 -3115 -3114 -3113 -3112 -3111 -3110 -3109 -3108 -3107 -3106 -3105 -3104 -3103 -3102 -3101 -3100 -3099 -3098 -3097 -3096 -3095 -3094 -3093 -3092 -3091 -3090 -3089 -3088 -3087 -3086 -3085 -3084 -3083 -3082 -3081 -3080 -3079 -3078 -3077 -3076 -3075 -3074 -3073 -3072 -3071 -3070 -3069 -3068 -3067 -3066 -3065 -3064 -3063 -3062 -3061 -3060 -3059 -3058 -3057 -3056 -3055 -3054 -3053 -3052 -3051 -3050 -3049 -3048 -3047 -3046 -3045 -3044 -3043 -3042 -3041 -3040 -3039 -3038 -3037 -3036 -3035 -3034 -3033 -3032 -3031 -3030 -3029 -3028 -3027 -3026 -3025 -3024 -3023 -3022 -3021 -3020 -3019 -3018 -3017 -3016 -3015 -3014 -3013 -3012 -3011 -3010 -3009 -3008 -3007 -3006 -3005 -3004 +3712 +3713 +3714 +3715 +3716 +3717 +3718 +3719 +3720 +3721 +3722 +3723 +3724 +3725 +3726 +3727 +3728 +3729 +3730 +3731 +3732 +3733 +3734 +3735 +3736 +3737 +3738 +3739 +3740 +3741 +3742 +3743 +3744 +3745 +3746 +3747 +3748 +3749 +3750 -917 -916 -915 -914 -913 -912 -911 -910 -909 -908 -907 -906 -905 -904 -903 -902 -901 -900 -899 -898 -897 -896 -895 -894 -893 -892 -891 -890 -889 -888 -887 -886 -885 -884 -883 -882 -881 -880 -879 -878 -877 -876 -875 -874 -873 -872 -871 -870 -869 -868 -867 -866 -865 -523 -522 -521 -520 -519 -518 -517 -516 -515 -514 -513 -512 -511 -510 -509 -508 -507 -506 -505 -504 -503 -502 -501 -500 -499 -498 -497 -496 -495 -494 -493 -492 -491 -490 -489 -488 -487 -486 -485 -484 -483 -482 -481 -480 -479 -478 -477 +3669 +3670 +3671 +3672 +3673 +3674 +3675 +3676 +3677 +3678 +116 +117 +118 +119 +120 +121 +122 +123 +124 +125 +126 +127 +128 +129 +130 +131 +132 +133 +134 +135 +136 +137 +138 +139 +140 +141 +142 +143 +144 +145 +146 +147 +148 +149 +150 +151 +152 +153 +154 +155 +156 +157 +158 +159 -715 -714 -713 -712 -711 -2951 -2950 -2949 -2948 -2947 -2946 -2945 -2944 -2943 -2942 -2941 -2940 -2939 -2938 -2937 -2936 -2935 -2934 -2933 -2932 -2931 -2930 -2929 -2928 -2927 -2926 -2925 -2924 -2923 -2922 -2921 -2920 -2919 -2918 -2917 -2916 -2915 -2914 -2913 -2912 -2911 -2910 -2909 -2908 -2907 -2906 -2905 -2904 -2903 -2902 +2791 +2792 +2793 +2794 +2795 +2796 +2797 +2798 +2799 +2800 +2801 +2802 +2803 +2804 +2805 +2806 +2807 +2808 +2809 +2810 +2811 +2812 +2813 +2814 +2815 +2816 +2817 +2818 +2819 +2820 +2821 +2822 +2823 +2824 +2825 +2826 +2827 +2828 +2829 +2830 +2831 +2832 +2833 +2834 +2835 +2836 +2837 +2838 +2839 +2840 +2841 +2842 +2843 +2844 +2845 +2846 +2847 +2848 +2849 +2850 +2851 +2852 +2853 +2854 +2855 +2856 +2857 +2858 +2859 +2860 +2861 +2862 +2863 +2864 +2865 +2866 +2867 +2868 +2869 +2870 +2871 +2872 +2873 +2874 +2875 +2876 +2877 +2878 +2879 +2880 +2881 +2882 +2883 +2884 +2885 +2886 +2887 +2888 +2889 +2890 +2891 +2892 +2893 +2894 +2895 +2896 +2897 +2898 +2899 +2900 +2901 -2790 -2789 -2788 -2787 -2786 -2785 -2784 -2783 -2782 -2781 -2780 -2779 -2778 -2777 -2776 -2775 -2774 -2773 -2772 -2771 -2770 -2769 -2768 -2767 -2766 -2765 -2764 -2763 -2762 -2761 -2760 -2759 -2758 -2757 -2756 -2755 -2754 -2753 -2752 -2751 -2750 -2749 -2748 -2747 -2746 -2745 -2744 -2743 -2742 -2741 -2740 -2739 -2738 -2737 -2736 -2735 -2734 -2733 -2732 -2731 -2730 -2729 -2728 -2727 -2726 -2725 -2724 -2723 -2722 -2721 -2720 -2719 -2718 -2717 -2716 -2715 -2501 -2500 -2499 -2498 -2497 -2496 -2495 -2494 -2493 -2492 -2491 -2490 -2489 -2488 -2487 -2486 -2485 -3801 -3800 -3799 -3798 -3797 -3796 -3795 -3794 -3793 -3792 -3791 -3790 -3789 -3788 -3787 -3786 -3785 -3784 -3783 -3782 -3781 -3780 -3779 -3778 -3777 -3776 -3775 -3774 -3773 -3772 -3771 -3770 -3769 -3768 -3767 -3766 -3765 -3764 -3763 -3762 -3761 -3760 -3759 -3758 -3757 -3756 -3755 -3754 -3753 -3752 -3751 +918 +919 +920 +921 +922 +923 +924 +925 +926 +927 +928 +929 +930 +3692 +3693 +3694 +3695 +3696 +3697 +3698 +3699 +3700 +3701 +3702 +3703 +3704 +1655 +1656 +1657 +1658 +1659 +1660 +1661 +1662 -2546 -2545 -2544 -2543 -2542 -2541 -2540 -2539 -2538 -2537 -2536 -2535 -2534 -2533 -2532 -2531 -2530 -2529 -2528 -2527 -2526 -2525 -2524 -2523 -2522 -2521 -2520 -2519 -2518 -2517 -2516 -2515 -2514 -2513 -2512 -2511 -2510 -2509 -2508 -2507 -2506 -1280 -1279 -1278 -1277 -1276 -1275 -1274 -1273 -1272 -1271 -1270 -1269 -1268 -1267 -1266 -1265 -1264 -1263 -1262 -1261 -1260 -1259 -1258 -1257 -1256 -1255 -1254 -1253 -1252 -1251 -1250 -1249 -1248 -1247 -1246 -1245 -1244 -1243 -1242 -1241 -1240 -1239 -1238 -1237 -1236 -1235 -1234 -1233 -1232 -1231 -1230 -1229 -1228 -1227 -1226 -1225 -1224 -1223 -1222 -1221 -1220 -1219 -1218 -1217 -1216 -1215 -1214 -1213 -1212 -1211 -1210 -1209 -1208 -1207 -1206 -1205 -1204 -1203 -1202 -1201 -1200 -1199 -1198 -1197 -1196 -1195 -1194 -1193 -1192 -1191 -1190 -1189 -1188 -1187 -1186 -1185 -1184 -1183 -1182 -1181 -1180 -1179 -1178 -1177 -1176 -1175 -1174 -1173 -1172 -1171 -1170 -1169 -1168 -1167 -1166 -1165 -1164 -1163 -1162 -1161 -1160 -1159 -1158 -1157 -1156 -1423 -1422 -1421 -1420 -1419 -1418 -1417 +1758 +1759 +1760 +1761 +1762 +1763 +1764 +1765 +1766 +1767 +1768 +1769 +1770 -1669 -1668 -1667 -1666 -1665 -1664 -1663 +2547 +2548 +2549 +2550 +2551 +2552 +2553 +2554 +2555 +2556 +2557 +2558 +2559 +2560 +2561 +2562 +2563 +2564 +2565 +2566 +2567 +3922 +3923 +3924 +3925 +3926 +3927 +3928 +3929 +3930 +3931 +3932 +3933 +3934 +3935 +3936 +3937 +3938 +3939 +3940 +3941 +3942 +3943 +3944 +3945 +3946 +3947 +3948 +3949 +3950 +3951 +3952 +3953 +3954 +3955 +3956 +3957 +3958 +1754 +1755 +1756 +1757 -1416 -1415 -1414 -1413 -1412 -1411 +3449 +3450 +3451 -326 -325 -324 -323 -322 -321 -320 -319 -318 -317 -316 -315 -314 -313 -312 -311 -310 -309 -308 -307 -306 -305 -304 -303 -302 -301 -300 -299 -298 -297 -296 -295 -294 -293 -369 -368 -367 -366 -365 -364 -363 -362 -361 -360 -359 -358 -357 -356 -355 -354 -353 -352 -351 -350 -349 -348 -347 -346 -345 -344 -343 -342 -341 -340 -339 -338 -337 -336 -335 -334 -333 -332 -331 -330 -329 -328 -327 +397 +398 +399 +400 +401 +402 +403 +404 +405 +406 +407 +408 +409 +410 +411 +412 +413 +414 +415 +416 +3382 +3383 +3384 +3385 +3386 +3387 +3388 +3389 +3390 +3391 +3392 +3393 +3394 +3395 +3396 +3397 +3398 +3399 +3400 +3401 +3402 +3403 +3404 +3405 +3406 +3344 +3345 +3346 +3347 +3348 +3349 +3350 +3351 +3352 +3353 +3354 +3355 +3356 +3357 +3358 +3359 +3360 +3361 +3362 +3363 +3364 +3365 +3366 +3367 +3368 +3369 +3370 +3371 +3372 +3373 +3374 +3375 +3376 +3377 +3378 +3379 +3380 +3381 +417 +418 +419 +420 +421 +422 +423 +424 +425 +426 +427 +428 +429 +430 +431 +432 +433 +434 +435 +436 +437 +438 +439 +440 +441 +442 +443 +444 +445 +446 +447 +448 +449 +450 +451 +452 +3522 +3523 +3524 +3525 +3526 +3527 +3528 +3529 +3530 +3531 +3532 +3533 +3534 +3535 +3536 +3537 +3538 -2446 -2445 -2444 -2443 -2442 -2441 -2440 -2439 -2438 -2437 -2436 -2435 -2434 -2433 -2432 -2048 -2047 -2046 -2045 -2044 -2043 -2042 -2041 -2040 -2039 -2038 -2037 -2036 -2035 -2034 -2033 -2032 -2031 -2030 -2029 -2028 -2027 -2026 -2025 -2024 -2023 -2022 -2021 -2020 -2019 -2018 -2017 -2016 -2015 -2014 -2013 -2012 -2011 -2010 -2009 -2008 -2007 -2006 -2005 -2004 -2003 -2002 -2001 -2000 -1999 -1998 -1997 -1996 -1995 -1994 -1993 -1992 -1991 -1990 -1989 -1988 -1987 -1986 -1985 -1984 -1983 -1982 -1981 -1980 -1979 -1978 -1977 -1976 -1975 -1974 -1973 -1972 -1971 -1970 -1969 -1968 -1967 -1966 -1965 -1964 -1963 -1962 -1961 -1960 -1959 -1958 -1957 -1956 -1955 -1954 -1953 -1952 -1951 -1950 -1949 -1948 -1947 -1946 -1945 -1944 -1943 -1942 -1941 -1940 -1939 -1938 -1937 -1936 -1935 -1934 -1933 -1932 -1931 -1930 -1929 -1928 -1927 -1926 -1925 -1924 -1923 -1922 -1921 -1920 -1919 -1918 -1917 -1916 -1915 -1914 -1913 -1912 -1911 -1910 -1909 -1908 -1907 -1906 -1905 -1904 -1903 -1902 -1901 -1900 -1899 -1898 -1897 -1896 -1895 +1837 +1838 +1839 +1840 +1841 +1842 +1843 +1844 +1845 +1846 +1847 +1848 +1849 +1850 +1851 +1852 +1853 +1854 +1855 +1856 +1857 +1858 +1859 +1860 +1861 +1862 +1863 +1864 +1865 +1866 +1867 +1868 +1869 +1870 +1871 +1872 +1873 +1874 +1875 +1876 +1877 +1878 +1879 +1880 +1881 +1882 +1883 +1884 +1885 +1886 +1887 +1888 +1889 +1890 +1891 +1892 +1893 +1894 -1836 -1835 -1834 -1833 -1832 -1831 -1830 -1829 -1828 -1827 -1826 -1825 -1824 -1823 -1822 -1821 -1820 -1819 -1818 -1817 -1816 -1815 -1814 -1813 -1812 -1811 -1810 -1809 -1808 -1807 -1806 -1805 -1804 -3920 -3919 -3918 -3917 -3916 -3915 -3914 -3913 -3912 -3911 -3910 -3909 -3908 -3907 -3906 -3905 -3904 -3903 -3902 -3901 -3900 -3899 -3898 -3897 -3896 +3974 +3975 +3976 +3977 +3978 +3979 +3980 +3981 +3982 +3983 +3984 +3985 +3986 +3987 +3988 +3989 +3990 +3991 +3992 +3993 +3994 +3995 +3996 +3997 +3998 +3999 +4000 +4001 +4002 +4003 +4004 +4005 +4006 +4007 +4008 +4009 +4010 +4011 +4012 +4013 +4014 +4015 +4016 +4017 +4018 +4019 +4020 +4021 +4022 +4023 +4024 +4025 +4026 +4027 +4028 +4029 +4030 +4031 +4032 +4033 +4034 +4035 +4036 +4037 +4038 +4039 +4040 +4041 +4042 +4043)"""))