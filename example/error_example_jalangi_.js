J$.iids = {"9":[1,6,1,7],"10":[4,12,4,15],"17":[1,6,1,7],"18":[8,13,8,39],"25":[1,1,1,7],"33":[2,10,2,11],"41":[2,10,2,11],"49":[2,10,2,11],"57":[4,12,4,13],"65":[4,14,4,15],"73":[4,12,4,15],"81":[4,5,4,15],"89":[3,1,5,2],"97":[3,1,5,2],"105":[3,1,5,2],"113":[3,1,5,2],"121":[7,14,7,17],"129":[7,18,7,20],"137":[7,21,7,23],"145":[7,14,7,24],"153":[7,14,7,24],"161":[7,1,7,25],"169":[8,1,8,8],"177":[8,13,8,27],"185":[8,29,8,39],"193":[8,1,8,40],"195":[8,1,8,12],"201":[8,1,8,41],"209":[1,1,8,41],"217":[1,1,8,41],"225":[3,1,5,2],"233":[1,1,8,41],"241":[3,1,5,2],"249":[3,1,5,2],"257":[1,1,8,41],"265":[1,1,8,41],"nBranches":0,"originalCodeFileName":"/Users/youssef/Documents/GitHub/TypescriptDoc-js/example/error_example.js","instrumentedCodeFileName":"/Users/youssef/Documents/GitHub/TypescriptDoc-js/example/error_example_jalangi_.js","code":"x1 = 0\nlet x2 = 1\nfunction sum(a, b){\n    return a+b\n}\n\nsum_result = sum(x1,x2);\nconsole.log(\"The sum is: \"+ sum_result);"};
jalangiLabel1:
    while (true) {
        try {
            J$.Se(209, '/Users/youssef/Documents/GitHub/TypescriptDoc-js/example/error_example_jalangi_.js', '/Users/youssef/Documents/GitHub/TypescriptDoc-js/example/error_example.js');
            function sum(a, b) {
                jalangiLabel0:
                    while (true) {
                        try {
                            J$.Fe(89, arguments.callee, this, arguments);
                            arguments = J$.N(97, 'arguments', arguments, 4);
                            a = J$.N(105, 'a', a, 4);
                            b = J$.N(113, 'b', b, 4);
                            return J$.X1(81, J$.Rt(73, J$.B(10, '+', J$.R(57, 'a', a, 0), J$.R(65, 'b', b, 0), 0)));
                        } catch (J$e) {
                            J$.Ex(241, J$e);
                        } finally {
                            if (J$.Fr(249))
                                continue jalangiLabel0;
                            else
                                return J$.Ra();
                        }
                    }
            }
            J$.N(217, 'x2', x2, 0);
            sum = J$.N(233, 'sum', J$.T(225, sum, 12, false, 89), 0);
            J$.X1(25, x1 = J$.W(17, 'x1', J$.T(9, 0, 22, false), J$.I(typeof x1 === 'undefined' ? undefined : x1), 4));
            let x2 = J$.X1(49, J$.W(41, 'x2', J$.T(33, 1, 22, false), x2, 3));
            J$.X1(161, sum_result = J$.W(153, 'sum_result', J$.F(145, J$.R(121, 'sum', sum, 1), 0)(J$.R(129, 'x1', x1, 2), J$.R(137, 'x2', x2, 1)), J$.I(typeof sum_result === 'undefined' ? undefined : sum_result), 4));
            J$.X1(201, J$.M(193, J$.R(169, 'console', console, 2), 'log', 0)(J$.B(18, '+', J$.T(177, "The sum is: ", 21, false), J$.R(185, 'sum_result', sum_result, 2), 0)));
        } catch (J$e) {
            J$.Ex(257, J$e);
        } finally {
            if (J$.Sr(265)) {
                J$.L();
                continue jalangiLabel1;
            } else {
                J$.L();
                break jalangiLabel1;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
