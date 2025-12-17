const fs = require('fs');
const path = require('path');
const glob = require('glob');

// Find all markdown files in docs directory
const files = glob.sync('docs/**/*.md', { cwd: __dirname });

files.forEach(file => {
    const filePath = path.join(__dirname, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Skip if it doesn't contain frontmatter (--- at the beginning)
    if (!content.startsWith('---')) return;
    
    // Extract frontmatter
    const frontmatterMatch = content.match(/---\n([\s\S]*?)\n---/);
    if (!frontmatterMatch) return;
    
    let frontmatter = frontmatterMatch[1];
    let originalFrontmatter = frontmatter;
    
    // Fix title
    frontmatter = frontmatter.replace(/^(title:\s*)(.+)$/m, (match, prefix, title) => {
        if (!title.trim().startsWith('"') && !title.trim().endsWith('"')) {
            // If title has a colon, wrap it in quotes
            if (title.includes(':')) {
                return `${prefix}"${title.replace(/"/g, '')}"`;
            }
        }
        return match;
    });
    
    // Fix learning objectives
    frontmatter = frontmatter.replace(/^(learning_objectives:\s*)$/m, '$1');
    const learningObjectivesRegex = /^(learning_objectives:\s*\n)([\s\S]*?)(\n\S)/m;
    if (frontmatter.match(learningObjectivesRegex)) {
        frontmatter = frontmatter.replace(learningObjectivesRegex, (match, prefix, objectives, suffix) => {
            // Add quotes to each list item that contains colons
            const fixedObjectives = objectives.replace(/(-\s*)(.*?)(?=\n|$)/g, (itemMatch, dash, content) => {
                if (content.includes(':') && !content.trim().startsWith('"')) {
                    return `${dash}"${content.replace(/"/g, '').trim()}"`;
                }
                return itemMatch;
            });
            return `${prefix}${fixedObjectives}${suffix}`;
        });
    }
    
    // Fix keywords
    frontmatter = frontmatter.replace(/^(keywords:\s*\[)([^\]]+)(\])/m, (match, start, keywords, end) => {
        // Split keywords by comma, trim whitespace, remove existing quotes, wrap in quotes, exclude empty strings
        const keywordArray = keywords.split(',').map(k => k.trim().replace(/"/g, '').replace(/^'|'$/g, ''));
        const filteredKeywords = keywordArray.filter(k => k && k.length > 0); // Remove empty strings
        const quotedKeywords = filteredKeywords.map(k => `"${k}"`);
        return `${start}${quotedKeywords.join(', ')}${end}`;
    });
    
    // Replace the frontmatter in the content
    if (frontmatter !== originalFrontmatter) {
        content = content.replace(/---\n[\s\S]*?\n---/, `---\n${frontmatter}\n---`);
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Fixed frontmatter in: ${file}`);
    }
});

console.log('Frontmatter fixing complete!');