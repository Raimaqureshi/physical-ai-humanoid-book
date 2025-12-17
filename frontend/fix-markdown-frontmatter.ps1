# Backup current state first
$docsPath = "E:\projects\hackathon-AI\speckit\frontend\docs"
$backupPath = "E:\projects\hackathon-AI\speckit\frontend\docs_backup"

if (Test-Path $backupPath) {
    Remove-Item -Path $backupPath -Recurse -Force
}

Copy-Item -Path $docsPath -Destination $backupPath -Recurse

Write-Host "Backup created at $backupPath"

# Get all markdown files
$mdFiles = Get-ChildItem -Path $docsPath -Recurse -Filter "*.md"

foreach ($file in $mdFiles) {
    $content = Get-Content $file.FullName -Raw
    
    # Only process files that have frontmatter
    if ($content -match '^---\r?\n([\s\S]*?)\r?\n---') {
        $frontmatter = $matches[1]
        $originalFrontmatter = $frontmatter
        
        # Fix title - wrap in quotes if it contains special characters
        $frontmatter = $frontmatter -replace '(?m)^title:\s*([^\r\n]*[,:][^\r\n]*)', 'title: "$1"'
        
        # Fix learning objectives - wrap items with colons in quotes
        $frontmatter = $frontmatter -replace '(?m)^(\s*-\s*)([^\r\n]*[,:][^\r\n]*)', '$1"$2"'
        
        # Fix keywords - process the array to wrap each value in quotes and handle colons properly
        $frontmatter = $frontmatter -replace '(?m)^keywords:\s*\[(.*?)\]', {
            param($match)
            $keywordsLine = $match.Value
            $keywordsContent = $keywordsLine -replace '^keywords:\s*\[(.*)\]$', '$1'

            # Split keywords by comma, clean each one, and reassemble
            $keywordArray = $keywordsContent -split ',' | ForEach-Object {
                $cleaned = $_.Trim().Trim('"').Trim("'")
                if ($cleaned -match ':') {
                    # If keyword contains a colon, split it and clean each part
                    $cleaned -split ':' | ForEach-Object {
                        $part = $_.Trim()
                        if ($part.Length -gt 0) { "`"$part`"" }
                    }
                } else {
                    if ($cleaned.Length -gt 0) { "`"$cleaned`"" }
                }
            } | Where-Object { $_ -ne $null }

            "keywords: [$($keywordArray -join ', ')]"
        }
        
        # Replace the frontmatter in the content if it was modified
        if ($frontmatter -ne $originalFrontmatter) {
            $newContent = $content -replace [regex]::Escape('---' + "`n" + $originalFrontmatter + "`n" + '---'), "---`n$frontmatter`n---"
            Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
            Write-Host "Fixed: $($file.FullName)"
        }
    }
}

Write-Host "Processing complete!"