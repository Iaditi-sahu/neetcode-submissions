from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegree = {}

        for i in range(len(recipes)):
            recipe = recipes[i]
            recipe_ingredients = ingredients[i]
            indegree[recipe] = len(recipe_ingredients)
            for ing in recipe_ingredients:
                adj[ing].append(recipe)

        q = deque(supplies)
        result = []

        while q:
            current = q.popleft()

            if current in indegree:
                result.append(current)

            for recipe in adj[current]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    q.append(recipe)

        return result
