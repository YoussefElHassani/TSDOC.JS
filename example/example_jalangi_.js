J$.iids = {"8":[10,8,10,15],"9":[2,5,2,12],"10":[9,14,9,18],"16":[9,14,9,18],"17":[2,17,2,22],"18":[9,20,9,23],"25":[2,5,2,23],"27":[2,5,2,16],"33":[2,5,2,23],"34":[9,20,9,23],"41":[1,1,3,2],"42":[10,8,10,11],"49":[1,1,3,2],"50":[10,8,10,15],"57":[6,5,6,12],"65":[6,17,6,22],"73":[6,5,6,23],"75":[6,5,6,16],"81":[6,5,6,23],"89":[5,1,7,2],"97":[5,1,7,2],"105":[9,11,9,12],"113":[9,11,9,12],"121":[9,11,9,12],"129":[9,14,9,15],"137":[9,16,9,18],"153":[9,20,9,21],"161":[9,20,9,23],"177":[10,8,10,9],"185":[10,10,10,11],"193":[10,14,10,15],"201":[11,9,11,12],"209":[11,9,11,14],"217":[11,9,11,15],"225":[13,9,13,12],"233":[13,9,13,14],"241":[13,9,13,15],"249":[17,1,17,8],"257":[17,13,17,19],"265":[17,1,17,20],"267":[17,1,17,12],"273":[17,1,17,20],"281":[1,1,17,20],"289":[1,1,3,2],"297":[1,1,17,20],"305":[5,1,7,2],"313":[1,1,17,20],"321":[1,1,17,20],"329":[1,1,3,2],"337":[1,1,3,2],"345":[5,1,7,2],"353":[5,1,7,2],"361":[10,5,14,6],"369":[9,1,15,2],"377":[9,1,15,2],"385":[1,1,17,20],"393":[1,1,17,20],"nBranches":4,"originalCodeFileName":"/Users/youssef/Documents/GitHub/TypescriptDoc-js/example/example.js","instrumentedCodeFileName":"/Users/youssef/Documents/GitHub/TypescriptDoc-js/example/example_jalangi_.js","code":"function foo(){\n    console.log(\"Foo\")\n}\n\nfunction bar(){\n    console.log(\"Bar\")\n}\n\nfor(var i=0; i<10; i++){\n    if(i%2===0){\n        foo();\n    } else{\n        bar();\n    }\n}\n\nconsole.log(\"done\")"};
jalangiLabel2:
    while (true) {
        try {
            J$.Se(281, '/Users/youssef/Documents/GitHub/TypescriptDoc-js/example/example_jalangi_.js', '/Users/youssef/Documents/GitHub/TypescriptDoc-js/example/example.js');
            function foo() {
                jalangiLabel0:
                    while (true) {
                        try {
                            J$.Fe(41, arguments.callee, this, arguments);
                            arguments = J$.N(49, 'arguments', arguments, 4);
                            J$.X1(33, J$.M(25, J$.R(9, 'console', console, 2), 'log', 0)(J$.T(17, "Foo", 21, false)));
                        } catch (J$e) {
                            J$.Ex(329, J$e);
                        } finally {
                            if (J$.Fr(337))
                                continue jalangiLabel0;
                            else
                                return J$.Ra();
                        }
                    }
            }
            function bar() {
                jalangiLabel1:
                    while (true) {
                        try {
                            J$.Fe(89, arguments.callee, this, arguments);
                            arguments = J$.N(97, 'arguments', arguments, 4);
                            J$.X1(81, J$.M(73, J$.R(57, 'console', console, 2), 'log', 0)(J$.T(65, "Bar", 21, false)));
                        } catch (J$e) {
                            J$.Ex(345, J$e);
                        } finally {
                            if (J$.Fr(353))
                                continue jalangiLabel1;
                            else
                                return J$.Ra();
                        }
                    }
            }
            foo = J$.N(297, 'foo', J$.T(289, foo, 12, false, 41), 0);
            bar = J$.N(313, 'bar', J$.T(305, bar, 12, false, 89), 0);
            J$.N(321, 'i', i, 0);
            for (var i = J$.X1(121, J$.W(113, 'i', J$.T(105, 0, 22, false), i, 3)); J$.X1(369, J$.C(16, J$.B(10, '<', J$.R(129, 'i', i, 1), J$.T(137, 10, 22, false), 0))); J$.X1(377, J$.B(34, '-', i = J$.W(161, 'i', J$.B(26, '+', J$.U(18, '+', J$.R(153, 'i', i, 1)), J$.T(145, 1, 22, false), 0), i, 2), J$.T(169, 1, 22, false), 0))) {
                if (J$.X1(361, J$.C(8, J$.B(50, '===', J$.B(42, '%', J$.R(177, 'i', i, 1), J$.T(185, 2, 22, false), 0), J$.T(193, 0, 22, false), 0)))) {
                    J$.X1(217, J$.F(209, J$.R(201, 'foo', foo, 1), 0)());
                } else {
                    J$.X1(241, J$.F(233, J$.R(225, 'bar', bar, 1), 0)());
                }
            }
            J$.X1(273, J$.M(265, J$.R(249, 'console', console, 2), 'log', 0)(J$.T(257, "done", 21, false)));
        } catch (J$e) {
            J$.Ex(385, J$e);
        } finally {
            if (J$.Sr(393)) {
                J$.L();
                continue jalangiLabel2;
            } else {
                J$.L();
                break jalangiLabel2;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
