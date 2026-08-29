class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Input: int[9,9] board
            Blank squares are "." in array
        Process: Find if board is valid
            Each row must contain 1-9 without duplicates
            Each column must contain 1-9 without duplicates
            Each of the nine 3x3 sub squares must contain 1-9 without duplicates
        Output: Return True if valid else False 

        Brute force: For each index check corresponding rows cols subsquares
        Optimal: Maintain sets/hashmaps for each row, col, subsquare

        Subsquares indices (3x3 subsquares)
        list0: 0 1 2 | 3 4 5 | 6 7 8
        list1: 0 1 2 | 3 4 5 | 6 7 8
        list2: 0 1 2 | 3 4 5 | 6 7 8

        list3: 0 1 2 | 3 4 5 | 6 7 8
        list4: 0 1 2 | 3 4 5 | 6 7 8
        list5: 0 1 2 | 3 4 5 | 6 7 8

        list6: 0 1 2 | 3 4 5 | 6 7 8
        list7: 0 1 2 | 3 4 5 | 6 7 8
        list8: 0 1 2 | 3 4 5 | 6 7 8

        Modulo row to find subsquare column
        Modulo column to find subsquare row
        '''
        # Key maps to row/column
        rowsSeen = defaultdict(set)
        colsSeen = defaultdict(set)
        subSquaresSeen = defaultdict(set)
        # iterate through rows
        for row in range(len(board)):
            # iterate through column in each row
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                # if in row return False
                if board[row][col] in rowsSeen[row]:
                    return False
                # else add to corresponding row
                else:
                    rowsSeen[row].add(board[row][col])

                # if in column return False
                if board[row][col] in colsSeen[col]:
                    return False
                # else add to corresponding column
                else:
                    colsSeen[col].add(board[row][col])

                # Modulo row and column to find subsquare
                subSquareRow = row // 3
                subSquareCol = col // 3
                # if in subsquare return False
                if board[row][col] in subSquaresSeen[(subSquareRow,subSquareCol)]:
                    return False
                # else add to corresponding subsquare
                else:
                    subSquaresSeen[(subSquareRow,subSquareCol)].add(board[row][col])

        return True
