class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = collections.defaultdict(list)

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                email_to_name[email] = name
                # Create bidirectional edges (Adjacency List)
                graph[first_email].append(email)
                graph[email].append(first_email)
                
        visited = set()
        result = []
        
        # DFS to find all connected emails
        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)
                    
        # Iterate through all emails to find connected components (1:16:59)
        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                # Sort emails and format as required
                result.append([email_to_name[email]] + sorted(component))
                
        return result