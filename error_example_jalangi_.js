J$.iids = {"9":[1,6,1,7],"10":[4,12,4,15],"17":[1,6,1,7],"18":[8,13,8,39],"25":[1,1,1,7],"33":[4,12,4,13],"41":[4,14,4,15],"49":[4,12,4,15],"57":[4,5,4,15],"65":[3,1,5,2],"73":[3,1,5,2],"81":[3,1,5,2],"89":[3,1,5,2],"97":[7,14,7,17],"105":[7,18,7,20],"113":[7,21,7,23],"121":[7,14,7,24],"129":[7,14,7,24],"137":[7,1,7,25],"145":[8,1,8,8],"153":[8,13,8,27],"161":[8,29,8,39],"169":[8,1,8,40],"171":[8,1,8,12],"177":[8,1,8,41],"185":[1,1,8,41],"193":[3,1,5,2],"201":[1,1,8,41],"209":[3,1,5,2],"217":[3,1,5,2],"225":[1,1,8,41],"233":[1,1,8,41],"nBranches":0,"originalCodeFileName":"/Users/youssef/Documents/GitHub/TypescriptDoc-js/error_example.js","instrumentedCodeFileName":"/Users/youssef/Documents/GitHub/TypescriptDoc-js/error_example_jalangi_.js","code":"x1 = 0\n\nfunction sum(a, b){\n    return a+b\n}\n\nsum_result = sum(x1,x2);\nconsole.log(\" The sum is:\"+ sum_result);"};
jalangiLabel1:
    while (true) {
        try {
            J$.Se(185, '/Users/youssef/Documents/GitHub/TypescriptDoc-js/error_example_jalangi_.js', '/Users/youssef/Documents/GitHub/TypescriptDoc-js/error_example.js');
            function sum(a, b) {
                jalangiLabel0:
                    while (true) {
                        try {
                            J$.Fe(65, arguments.callee, this, arguments);
                            arguments = J$.N(73, 'arguments', arguments, 4);
                            a = J$.N(81, 'a', a, 4);
                            b = J$.N(89, 'b', b, 4);
                            return J$.X1(57, J$.Rt(49, J$.B(10, '+', J$.R(33, 'a', a, 0), J$.R(41, 'b', b, 0), 0)));
                        } catch (J$e) {
                            J$.Ex(209, J$e);
                        } finally {
                            if (J$.Fr(217))
                                continue jalangiLabel0;
                            else
                                return J$.Ra();
                        }
                    }
            }
            sum = J$.N(201, 'sum', J$.T(193, sum, 12, false, 65), 0);
            J$.X1(25, x1 = J$.W(17, 'x1', J$.T(9, 0, 22, false), J$.I(typeof x1 === 'undefined' ? undefined : x1), 4));
            J$.X1(137, sum_result = J$.W(129, 'sum_result', J$.F(121, J$.R(97, 'sum', sum, 1), 0)(J$.R(105, 'x1', x1, 2), J$.R(113, 'x2', x2, 2)), J$.I(typeof sum_result === 'undefined' ? undefined : sum_result), 4));
            J$.X1(177, J$.M(169, J$.R(145, 'console', console, 2), 'log', 0)(J$.B(18, '+', J$.T(153, " The sum is:", 21, false), J$.R(161, 'sum_result', sum_result, 2), 0)));
        } catch (J$e) {
            J$.Ex(225, J$e);
        } finally {
            if (J$.Sr(233)) {
                J$.L();
                continue jalangiLabel1;
            } else {
                J$.L();
                break jalangiLabel1;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
