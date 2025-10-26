#!/bin/bash

echo "🚀 Running comprehensive code quality checks..."
echo "=================================================="
echo ""

echo "🔍 1. Running ESLint check..."
echo "------------------------------"
if npm run lint:check; then
    echo "✅ ESLint: No issues found!"
else
    echo "❌ ESLint: Issues found, attempting auto-fix..."
    echo ""
    echo "🔧 2. Running ESLint auto-fix..."
    echo "--------------------------------"
    npm run lint:fix
    echo ""
    echo "🔍 3. Re-checking after auto-fix..."
    echo "-----------------------------------"
    if npm run lint:check; then
        echo "✅ ESLint: All auto-fixable issues resolved!"
    else
        echo "⚠️ ESLint: Some issues require manual fixing:"
        npm run lint
    fi
fi

echo ""
echo "🎨 4. Running Prettier check..."
echo "-------------------------------"
if npm run format:check; then
    echo "✅ Prettier: Code is properly formatted!"
else
    echo "🔧 Prettier: Formatting code..."
    npm run format
    echo "✅ Prettier: Code formatting completed!"
fi

echo ""
echo "🎉 Code quality check completed!"
echo "================================"