class Solution(object):
    def twoCitySchedCost(self, costs):
        # Step 1: Sort by the difference (Cost_B - Cost_A)
        # Jinka difference sabse negative hoga, woh list mein sabse aage aayenge
        costs.sort(key=lambda x: x[1] - x[0])
        
        n = len(costs) // 2
        total_cost = 0
        
        # Step 2: Pehle aadhe logon ko City B bhejo (Kyunki B unke liye relatively sasta hai)
        for i in range(n):
            total_cost += costs[i][1] # City B ka cost add karo
            
        # Step 3: Baaki bache aadhe logon ko City A bhejo
        for i in range(n, 2 * n):
            total_cost += costs[i][0] # City A ka cost add karo
            
        return total_cost