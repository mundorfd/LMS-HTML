# Canvas Design Library - Style Guide Structure

## Overview

This Canvas Design Library provides ready-to-use HTML components with inline styles for Canvas LMS course development. All components are designed for AA 2.1 accessibility compliance and easy maintenance in the Canvas Rich Content Editor (RCE).

## File Structure

Each style guide page follows a consistent documentation format to ensure usability and maintainability.

### Page Layout

```html
<div style="width: 98%; max\-width: 1000px; margin-bottom: 24px;">
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

### OSU Brand Color Palette

- **Beaver Orange**: #dc4405 (Primary brand color)
- **Pine Stand Green**: #4A773C (Secondary/supporting content)
- **Star Canvas Blue**: #003b5c (Technical content, quotes)
- **Stratosphere Blue**: #006A8E (Processes, workflows)
- **Luminance Yellow**: #FFB500 (Warnings, highlights - use black text for contrast)

### Accessibility Requirements

- **Text contrast**: Minimum 4.5:1 ratio for text under 18pt (or bold 14pt)
- **Proper heading hierarchy**: No skipping levels (h1→h2→h3→h4→h5)
- **Default link colors**: Use browser defaults, no custom link styling
- **Decorative elements**: Mark with aria-hidden="true"
- **Semantic HTML**: Proper heading structure, list markup, blockquote elements
- **Subtitle text**: #555 minimum (not #888 or lighter)
- **Body text**: #666 or darker for sufficient contrast

### Canvas Dark Mode Compatibility

Canvas users can switch between light and dark themes, but custom styling can create accessibility issues in dark mode:

- **Light backgrounds with custom colors**: When you add light background colors (like #fefefe), always enforce dark text by adding `color: #2D3B45;` (Canvas regular text color)
- **Recommended light background**: Use #fefefe instead of lighter grays - provides optimal contrast with OSU Beaver Orange (#D73F09) links in both light and dark modes
- **Avoid very light backgrounds**: Colors like #fafbfc, #fcfcfb, or #f8f9fa may not provide adequate contrast with default link colors
- **Dark backgrounds are safe**: Text boxes with dark backgrounds and light text are not affected by Canvas dark mode changes

**Example of dark mode compatible styling:**
```css
background-color: #fefefe; color: #2D3B45;
```

This ensures text remains readable in both Canvas light and dark themes while maintaining proper contrast ratios.

### Canvas Compatibility

- **Inline styles only**: No external CSS dependencies
- **RCE-friendly**: Maintains formatting when edited in Canvas
- **Copy-paste ready**: All code blocks can be directly used
- **Built-in class support**: Leverages Canvas classes when available (pill, dl-horizontal, etc.)

## Component Evaluation Framework

When assessing new design snippets for inclusion:

### Design Principles (Robin Williams)

- **Contrast**: Creates clear visual hierarchy
- **Repetition**: Fits with existing design system
- **Alignment**: Clean and organized layout
- **Proximity**: Related elements grouped logically

### Accessibility Checklist

- ✅ 4.5:1 contrast ratios for all text
- ✅ Proper heading hierarchy (no skipping)
- ✅ Semantic HTML structure
- ✅ Color-independent emphasis
- ✅ Screen reader compatibility

### Pedagogical Value

- ✅ Enhances learning or serves clear instructional purpose
- ✅ Appropriate for Canvas learning environment
- ✅ Fills gap in existing component library

### Maintenance Feasibility

- ✅ Simple enough for non-technical instructors
- ✅ Compatible with Canvas RCE editing workflows
- ✅ Uses established color palette and patterns

## Best Practices

### Documentation

1. Include live previews for every component
2. List all key CSS properties in "Ingredients"
3. Provide 4-6 practical use cases
4. Use consistent naming conventions
5. Include accessibility notes where relevant

### Code Quality

1. Format HTML with proper indentation
2. Keep CSS properties grouped logically
3. Use semantic HTML elements
4. Include accessibility attributes (aria-hidden, scope, etc.)
5. Test contrast ratios for all color combinations

### Maintenance

1. Update "Last updated" dates when modifying
2. Test components in Canvas RCE before publishing
3. Verify color contrast meets AA standards
4. Keep component variations minimal but useful
5. Document any Canvas-specific classes or dependencies

## File Naming Convention

- Use descriptive, lowercase names
- Separate words with hyphens or spaces
- Include "Components" or "Box" in component collections
- Examples: `Blue Information Box.html`, `Definition Lists & Structured Content.html`

## Adding New Components

When creating new components:

1. **Follow the exact structure** outlined above
2. **Use the established OSU color palette** 
3. **Ensure AA 2.1 accessibility compliance**
4. **Test in Canvas RCE environment**
5. **Include comprehensive documentation**
6. **Add creation date and library footer**
7. **Verify heading hierarchy** (no skipping levels)
8. **Test contrast ratios** for all text/background combinations
9. **Use semantic HTML** structures appropriate to content type
10. **Mark decorative elements** with aria-hidden="true"

This structure ensures consistency, accessibility, and maintainability across the entire Canvas Design Library while serving the pedagogical needs of OSU course development.

## Future Design Components (Planned)

### Typography & Text Elements

- **Drop Caps** - Decorative first letter styling for articles/chapters
- **Blockquotes** - Styled quote containers with attribution options
- **Pull Quotes** - Highlighted excerpts for emphasis
- **Lists** - Enhanced bullet/numbered lists with OSU styling
- **Horizontal Rules (HR)** - Section dividers with OSU branding
- **Captions** - Styled text for images and media
- **Bylines** - Author/date attribution styling

### Layout & Structure

- **Column Layouts** - 2-column, 3-column text arrangements
- **Card Components** - Content cards with headers/footers
- **Accordion/Toggle** - Expandable content sections
- **Tabs** - Horizontal navigation between content sections
- **Sidebar Components** - Left/right content sidebars
- **Grid Systems** - Responsive layout containers

### Interactive Elements

- **Button Variations** - Different sizes, styles, states
- **Link Styling** - Enhanced link appearances and hover states
- **Form Elements** - Styled inputs, selectors, checkboxes
- **Navigation Menus** - Course navigation styling
- **Breadcrumbs** - Path navigation components

### Media & Visual

- **Image Containers** - Styled photo/graphic frames
- **Video Wrappers** - Responsive video containers
- **Gallery Layouts** - Multi-image display options
- **Icon Integration** - OSU-branded icon usage
- **Progress Bars** - Course/module progress indicators

### Specialized Content

- **Timeline Components** - Chronological content display
- **FAQ Sections** - Question/answer styling
- **Testimonials** - Student/faculty quote boxes
- **Statistics Displays** - Number/data highlighting
- **Code Blocks** - Syntax-highlighted code samples
- **Definition Lists** - Glossary-style term/definition pairs

### Course-Specific

- **Assignment Boxes** - Structured assignment layouts
- **Rubric Components** - Grading criteria displays
- **Schedule/Calendar** - Course timeline elements
- **Resource Links** - Enhanced link collections
- **Discussion Prompts** - Styled question frameworks
- **Module Headers** - Section introduction styling
