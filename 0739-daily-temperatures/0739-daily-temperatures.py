class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        st =[]
        for i in range(len(temperatures)):
            while st and temperatures[i]>temperatures[st[-1]]:
                j= st.pop()
                res[j] = i-j
            st.append(i)
        return res    


        