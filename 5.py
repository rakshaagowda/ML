def minmax(depth, nodeindex, ismaximizing, scores, h):
    if depth == h:
        return scores[nodeindex]
    if ismaximizing:
        return max(minmax(depth+1,nodeindex*2,False,scores,h),
                   minmax(depth+1,nodeindex*2+1,False,scores,h)
                   )
    else:
        return min(minmax(depth+1,nodeindex*2,True,scores,h),
                   minmax(depth+1,nodeindex*2+1,True,scores,h)
                   )
def alphabeta(depth, nodeindex, ismaximizing, scores, h,alpha,beta):
    if depth == h:
        return scores[nodeindex]
    if ismaximizing:
        left=alphabeta(depth+1,nodeindex*2,False,scores,h,alpha,beta)
        alpha=max(alpha,left)
        if beta<=alpha:
            return left
        right= alphabeta(depth+1,nodeindex*2+1,False,scores,h,alpha,beta)
        return max(alpha,right)
                   
    else:
        left=alphabeta(depth+1,nodeindex*2,True,scores,h,alpha,beta)
        beta=min(beta,left)
        if beta<=alpha:
            return left
        right= alphabeta(depth+1,nodeindex*2+1,True,scores,h,alpha,beta)
        return min(beta,right)
        
                   
print("enter the depth of tree:")
h=int(input())
print("entr the scoresseparated by space:")
scores_input = input()
scores=list(map(int,scores_input.split()))
optimal_value = minmax(0, 0, True, scores, h)
print("The optimal value is:", optimal_value)
optimal_value_ab = alphabeta(0, 0, True, scores, h, float('-inf'), float('inf'))
print(f"Optimal value using Alpha-Beta Pruning: {optimal_value_ab}")