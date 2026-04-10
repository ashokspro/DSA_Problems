package Striver;

public class RemoveOutermostParenthesesSolved {
    public String removeOuterParentheses(String s) {
        StringBuilder res = new StringBuilder();
        int opened = 0;
        for (char c: s.toCharArray()){
            if (c == '(' && 0 < opened++) res.append(c);
            if (c == ')' && 1 < opened--) res.append(c);
        }
    return res.toString();
    }
}
