# Canvas Design Library - Style Guide Structure

## Overview

This Canvas Design Library provides ready-to-use HTML components with inline styles for Canvas LMS course development. All components are designed for AA 2.1 accessibility compliance and easy maintenance in the Canvas Rich Content Editor (RCE).

## File Structure

Each style guide page follows a consistent documentation format to ensure usability and maintainability.

### Page Layout

```html
<div style="width: 98%; max-width: 1000px; margin-bottom: 24px;">
    <!-- Page Header -->
    <!-- Component Sections -->
    <!-- Footer -->
</div>
```

## Standard Page Structure

### 1. Page Header
Every page begins with a standardized header section:

```html
<div style="border-bottom: 3px solid #dc4405; padding-bottom: 20px; margin-bottom: 30px;">
    <h2 style="color: #666; margin: 10px 0 0 0; font-size: 16pt;">[Component Category]</h2>
    <p style="margin: 10px 0 0 0; color: #555;">[Brief description of component purpose]</p>
</div>
```

**Required Elements:**
- **H2 heading** (16pt, #666 color) - Main component category
- **Subtitle paragraph** (#555 color for accessibility) - Brief description
- **Border styling** (3px solid #dc4405) - Consistent visual separation

### 2. Component Sections
Each individual component follows this structure:

```html
<div id="[component-id]" style="margin-bottom: 50px; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
    <!-- Component Header -->
    <!-- Component Body -->
</div>
```

#### Component Header
```html
<div style="background: #f5f5f5; padding: 15px 20px; border-bottom: 1px solid #e0e0e0;">
    <h3 style="margin: 0; color: #333;">[Component Name]</h3>
    <p style="margin: 5px 0 0 0; color: #666;">[Component description]</p>
</div>
```

#### Component Body
```html
<div style="padding: 20px;">
    <!-- Preview Section -->
    <!-- Ingredients Section -->
    <!-- HTML/CSS Code Section -->
    <!-- Suggested Uses Section -->
    <!-- Creation Date Section -->
</div>
```

### 3. Required Subsections

#### Preview Section
```html
<div style="margin-bottom: 25px;">
    <h4>Preview:</h4>
    [Live component demonstration]
</div>
```

#### Ingredients Section
```html
<h4>Ingredients:</h4>
<ul>
    <li><strong>property:</strong> value explanation</li>
    <!-- List all key CSS properties and their purposes -->
</ul>
```

#### HTML/CSS Code Section
```html
<h4>HTML/CSS Code:</h4>
<pre style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 4px; padding: 15px; font-family: 'Courier New', monospace; font-size: 12px; overflow-x: auto; white-space: pre-wrap; margin: 10px 0;">
[Formatted HTML code block]
</pre>
```

#### Suggested Uses Section
```html
<h4>Suggested Uses:</h4>
<ul>
    <li>[Use case 1]</li>
    <li>[Use case 2]</li>
    <!-- 4-6 practical applications -->
</ul>
```

#### Creation Date Section
```html
<div style="background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 4px; padding: 10px; margin: 15px 0; font-size: 12px;">
    <strong>Date Created:</strong> [Date]
</div>
```

### 4. Page Footer
Every page ends with this standardized footer:

```html
<div style="border-top: 2px solid #e0e0e0; padding-top: 20px; margin-top: 40px; text-align: center; color: #666;">
    <p><strong>Canvas Design Library</strong> | Created [Date] | Last updated: [Date]</p>
    <p>For use in OSU Canvas course development | Components designed for accessibility and consistency</p>
</div>
```

## Design Standards

### Heading Hierarchy
- **H2** (16pt, #666): Page/category title
- **H3** (#333): Component name
- **H4**: Section headings (Preview, Ingredients, etc.)
- **H5**: Sub-variations or examples

### Color Palette
- **Primary Red**: #d73f09
- **Green**: #4A773C  
- **Teal**: #00859B
- **Yellow**: #FFB500
- **Blue**: #006A8E

### Accessibility Requirements
- **Text contrast**: Minimum AA 2.1 compliance
- **Subtitle text**: #555 (not #888)
- **Body text**: #666 or darker
- **Semantic HTML**: Proper heading structure, alt text, etc.

### Canvas Compatibility
- **Inline styles only**: No external CSS dependencies
- **RCE-friendly**: Maintains formatting when edited in Canvas
- **Copy-paste ready**: All code blocks can be directly used

## Best Practices

### Documentation
1. Include live previews for every component
2. List all key CSS properties in "Ingredients"
3. Provide 4-6 practical use cases
4. Use consistent naming conventions

### Code Quality
1. Format HTML with proper indentation
2. Keep CSS properties grouped logically
3. Use semantic HTML elements
4. Include accessibility attributes (scope, alt, etc.)

### Maintenance
1. Update "Last updated" dates when modifying
2. Test components in Canvas RCE before publishing
3. Verify color contrast meets AA standards
4. Keep component variations minimal but useful

## File Naming Convention

- Use descriptive, lowercase names
- Separate words with hyphens or spaces
- Include "Components" or "Box" in component collections
- Examples: `Blue Information Box.html`, `Pro-Tip Components.html`

## Adding New Components

When creating new components:

1. Follow the exact structure outlined above
2. Use the established color palette
3. Ensure AA 2.1 accessibility compliance
4. Test in Canvas RCE environment
5. Include comprehensive documentation
6. Add creation date and library footer

This structure ensures consistency, accessibility, and maintainability across the entire Canvas Design Library.