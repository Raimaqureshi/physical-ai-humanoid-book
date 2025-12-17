const fs = require('fs');
const path = require('path');

// Get all markdown files in docs directory
const docsDir = './docs';

function getAllMdFiles(dir) {
  let results = [];
  const items = fs.readdirSync(dir);

  items.forEach(item => {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      results = results.concat(getAllMdFiles(fullPath));
    } else if (path.extname(fullPath) === '.md') {
      results.push(fullPath);
    }
  });

  return results;
}

const mdFiles = getAllMdFiles(docsDir);

console.log(`Found ${mdFiles.length} markdown files`);

mdFiles.forEach(filePath => {
  try {
    let content = fs.readFileSync(filePath, 'utf8');

    // Check if file starts with frontmatter
    if (!content.startsWith('---\n')) {
      return;
    }

    // Find the end of frontmatter (second occurrence of ---)
    const frontmatterEndIndex = content.indexOf('\n---\n', 4);
    if (frontmatterEndIndex === -1) {
      return; // No proper frontmatter found
    }

    const frontmatter = content.substring(4, frontmatterEndIndex);
    const restOfContent = content.substring(frontmatterEndIndex + 5);

    // Process frontmatter to fix YAML issues
    let processedFrontmatter = frontmatter;

    // Quote titles that contain special characters
    processedFrontmatter = processedFrontmatter.replace(/^(title:)(.+)$/m, (match, prefix, title) => {
      title = title.trim();
      if (title.includes(':') || title.includes(',')) {
        if (!title.startsWith('"') && !title.endsWith('"')) {
          return `${prefix} "${title}"`;
        }
      }
      return match;
    });

    // Quote learning_objectives that contain special characters
    processedFrontmatter = processedFrontmatter.replace(/^(learning_objectives:\s*\n)((?:\s*- .*\n)*)/m, (match, prefix, objectivesList) => {
      const fixedObjectives = objectivesList.replace(/(\s*- )(.+)$/gm, (itemMatch, dash, objective) => {
        objective = objective.trim();
        if (objective.includes(':')) {
          if (!objective.startsWith('"') && !objective.endsWith('"')) {
            return `${dash}"${objective}"`;
          }
        }
        return itemMatch;
      });
      return `${prefix}${fixedObjectives}`;
    });

    // Fix keywords array - handle individual keywords that contain colons
    processedFrontmatter = processedFrontmatter.replace(/^(keywords:)(\s*\[.*\])/m, (match, prefix, keywordsPart) => {
      // Extract keywords from the array
      const arrayMatch = keywordsPart.match(/\[(.*)\]/);
      if (!arrayMatch) return match;
      
      let keywords = arrayMatch[1];
      const keywordArray = keywords.split(',').map(k => k.trim().replace(/^"/, '').replace(/"$/, ''));
      
      // Process each keyword
      const processedKeywords = keywordArray.map(kw => {
        // If a keyword contains a colon, split it and add each part
        if (kw.includes(':')) {
          return kw.split(':').map(part => part.trim()).filter(part => part.length > 0).map(part => `"${part}"`);
        }
        return kw.length > 0 ? `"${kw}"` : null;
      }).filter(kw => kw !== null);
      
      // Flatten array if needed
      const finalKeywords = [];
      processedKeywords.forEach(kw => {
        if (Array.isArray(kw)) {
          finalKeywords.push(...kw);
        } else {
          finalKeywords.push(kw);
        }
      });

      return `${prefix} [${finalKeywords.join(', ')}]`;
    });

    // Only write if frontmatter was modified
    if (processedFrontmatter !== frontmatter) {
      const newContent = `---\n${processedFrontmatter}---\n${restOfContent}`;
      fs.writeFileSync(filePath, newContent, 'utf8');
      console.log(`Fixed frontmatter in: ${filePath}`);
    }
  } catch (error) {
    console.error(`Error processing file ${filePath}:`, error.message);
  }
});

console.log('Finished processing all markdown files');