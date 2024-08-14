class Questions:

    def LCS(self, text1, text2):
        """
        1143: Leetcode -> Longest Common Subsequence
        """

        def _lcs_r(t1, t2, i, j):
            if i == len(t1) or j == len(t2):
                return 0

            ans = 0
            if t1[i] == t2[j]:
                ans = 1 + _lcs_r(t1, t2, i + 1, j + 1)
            else:
                ans = 0 + max(_lcs_r(t1, t2, i, j + 1), _lcs_r(
                    t1, t2, i + 1, j))

            return ans

        def _lcs_m(t1, t2, i, j, dp):
            if i == len(t1) or j == len(t2):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            if t1[i] == t2[j]:
                ans = 1 + _lcs_m(t1, t2, i + 1, j + 1, dp)
            else:
                ans = 0 + max(_lcs_m(t1, t2, i, j + 1, dp),
                              _lcs_m(t1, t2, i + 1, j, dp))

            dp[i][j] = ans

            return dp[i][j]

        def _lcs_t(t1, t2):
            dp = [[0 for _ in range(len(text2) + 1)]
                  for _ in range(len(text1) + 1)]

            for i in range(len(t1) - 1, -1, -1):
                for j in range(len(t2) - 1, -1, -1):
                    ans = 0
                    if t1[i] == t2[j]:
                        ans = 1 + dp[i + 1][j + 1]
                    else:
                        ans = 0 + max(dp[i][j + 1], dp[i + 1][j])

                    dp[i][j] = ans
            return dp[0][0]

        def _lcs_so(t1, t2):
            curr = [0 for _ in range(len(t2) + 1)]
            next = [0 for _ in range(len(t2) + 1)]

            for i in range(len(t1) - 1, -1, -1):
                for j in range(len(t2) - 1, -1, -1):
                    ans = 0
                    if t1[i] == t2[j]:
                        ans = 1 + next[j + 1]
                    else:
                        ans = 0 + max(curr[j + 1], next[j])

                    curr[j] = ans
                next = curr.copy()
            return next[0]

        i = 0
        j = 0

        # # Recursion
        # ans = _lcs_r(text1, text2, i, j)

        # # DP: Memoization
        # dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        # ans = _lcs_m(text1, text2, i, j, dp)

        # # DP: Tabulation
        # ans = _lcs_t(text1, text2)

        # Space optimization
        ans = _lcs_so(text1, text2)

        return ans

    def palindromic_subsequence(self, s="abbccccbbabadaadfa"):
        """
        516: Leetcode -> Longest Palindromic Subsequence.
        """

        def _lps_r(t1, t2, i, j):
            if i == len(t1) or j == len(t2):
                return 0

            ans = 0
            if t1[i] == t2[j]:
                ans = 1 + _lps_r(t1, t2, i + 1, j + 1)
            else:
                ans = 0 + max(_lps_r(t1, t2, i, j + 1), _lps_r(
                    t1, t2, i + 1, j))

            return ans

        def _lps_m(t1, t2, i, j, dp):
            if i == len(t1) or j == len(t2):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            if t1[i] == t2[j]:
                ans = 1 + _lps_m(t1, t2, i + 1, j + 1, dp)
            else:
                ans = 0 + max(_lps_m(t1, t2, i, j + 1, dp),
                              _lps_m(t1, t2, i + 1, j, dp))

            dp[i][j] = ans

            return dp[i][j]

        def _lcs_t(t1, t2):
            "HW"

        def _lcs_so(t1, t2):
            "HW"

        str1 = s
        str2 = s[::-1]
        i = 0
        j = 0

        # # Recursion
        # ans = _lps_r(str1, str2)

        # DP: Memoziation
        dp = [[-1 for _ in range(len(str2))] for _ in range(len(str1))]
        ans = _lps_m(str1, str2, i, j, dp)

        return ans

    def edit_distance(self, word1, word2):
        """
        72: Leetcode -> Edit Distance
        """

        def _minD_r(w1, w2, i, j):
            # base case
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1) - i

            ans = 0
            if w1[i] == w2[j]:
                ans = _minD_r(w1, w2, i + 1, j + 1)
            else:
                insertAns = 1 + _minD_r(w1, w2, i, j + 1)
                deleteAns = 1 + _minD_r(w1, w2, i + 1, j)
                replaceAns = 1 + _minD_r(w1, w2, i + 1, j + 1)

                ans = min(insertAns, deleteAns, replaceAns)

            return ans

        def _minD_m(w1, w2, i, j, dp):
            # base case
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1) - i

            if dp[i][j] != -1:
                return dp[i][j]

            if w1[i] == w2[j]:
                dp[i][j] = _minD_m(w1, w2, i + 1, j + 1, dp)
            else:
                insertAns = 1 + _minD_m(w1, w2, i, j + 1, dp)
                deleteAns = 1 + _minD_m(w1, w2, i + 1, j, dp)
                replaceAns = 1 + _minD_m(w1, w2, i + 1, j + 1, dp)

                dp[i][j] = min(insertAns, deleteAns, replaceAns)

            return dp[i][j]

        def _minD_t(w1, w2):
            dp = [[0 for _ in range(len(w2) + 1)] for _ in range(len(w1) + 1)]

            for j in range(len(w2)):
                dp[len(w1)][j] = len(w2) - j

            for i in range(len(w1)):
                dp[i][len(w2)] = len(w1) - i

            for i in range(len(w1) - 1, -1, -1):
                for j in range(len(w2) - 1, -1, -1):
                    if w1[i] == w2[j]:
                        ans = dp[i + 1][j + 1]
                    else:
                        insertAns = 1 + dp[i][j + 1]
                        deleteAns = 1 + dp[i + 1][j]
                        replaceAns = 1 + dp[i + 1][j + 1]

                        ans = min(insertAns, deleteAns, replaceAns)
                    dp[i][j] = ans

            return dp[0][0]

        def _minD_so(w1, w2):

            curr = [0 for _ in range(len(w2) + 1)]
            next = [0 for _ in range(len(w2) + 1)]

            for j in range(len(w2)):
                next[j] = len(w2) - j

            for i in range(len(w1) - 1, -1, -1):
                for j in range(len(w2) - 1, -1, -1):
                    curr[len(w2)] = len(w1) - i
                    ans = 0
                    if w1[i] == w2[j]:
                        ans = next[j + 1]
                    else:
                        insertAns = 1 + curr[j + 1]
                        deleteAns = 1 + next[j]
                        replaceAns = 1 + next[j + 1]

                        ans = min(insertAns, deleteAns, replaceAns)
                    curr[j] = ans
                next = curr[:]

            return next[0]

        if not len(word1):
            return len(word2)

        if not len(word2):
            return len(word1)

        # # Recursion
        # ans = _minD_r(word1, word2, 0, 0)

        # # DP: Memoization
        # dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        # ans = _minD_m(word1, word2, 0, 0, dp)

        # # DP: Tabulation
        # ans = _minD_t(word1, word2)

        # Space optimization
        ans = _minD_so(word1, word2)

        return ans
