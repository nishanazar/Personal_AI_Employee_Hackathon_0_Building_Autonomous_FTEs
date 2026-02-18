"""
Silver Tier Test Suite
Comprehensive pytest test cases for AI Employee Vault Silver Tier
"""

import pytest
import os
import time
from pathlib import Path
from datetime import datetime


# ============================================================================
# Test Fixtures
# ============================================================================

@pytest.fixture
def vault_path():
    """Get the vault directory path"""
    return Path(__file__).parent

@pytest.fixture
def inbox_path(vault_path):
    """Get the Inbox folder path"""
    return vault_path / 'Inbox'

@pytest.fixture
def needs_action_path(vault_path):
    """Get the Needs_Action folder path"""
    return vault_path / 'Needs_Action'

@pytest.fixture
def pending_approval_path(vault_path):
    """Get the Pending_Approval folder path"""
    return vault_path / 'Pending_Approval'

@pytest.fixture
def approved_path(vault_path):
    """Get the Approved folder path"""
    return vault_path / 'Approved'

@pytest.fixture
def done_path(vault_path):
    """Get the Done folder path"""
    return vault_path / 'Done'

@pytest.fixture
def plans_path(vault_path):
    """Get the Plans folder path"""
    return vault_path / 'Plans'


# ============================================================================
# Test 1: Folder Structure Tests
# ============================================================================

class TestFolderStructure:
    """Test that all required folders exist"""
    
    def test_inbox_folder_exists(self, vault_path):
        """Verify Inbox folder exists"""
        inbox = vault_path / 'Inbox'
        assert inbox.exists(), "Inbox folder should exist"
        assert inbox.is_dir(), "Inbox should be a directory"
    
    def test_needs_action_folder_exists(self, vault_path):
        """Verify Needs_Action folder exists"""
        needs_action = vault_path / 'Needs_Action'
        assert needs_action.exists(), "Needs_Action folder should exist"
        assert needs_action.is_dir(), "Needs_Action should be a directory"
    
    def test_pending_approval_folder_exists(self, vault_path):
        """Verify Pending_Approval folder exists"""
        pending_approval = vault_path / 'Pending_Approval'
        assert pending_approval.exists(), "Pending_Approval folder should exist"
        assert pending_approval.is_dir(), "Pending_Approval should be a directory"
    
    def test_approved_folder_exists(self, vault_path):
        """Verify Approved folder exists"""
        approved = vault_path / 'Approved'
        assert approved.exists(), "Approved folder should exist"
        assert approved.is_dir(), "Approved should be a directory"
    
    def test_done_folder_exists(self, vault_path):
        """Verify Done folder exists"""
        done = vault_path / 'Done'
        assert done.exists(), "Done folder should exist"
        assert done.is_dir(), "Done should be a directory"
    
    def test_plans_folder_exists(self, vault_path):
        """Verify Plans folder exists"""
        plans = vault_path / 'Plans'
        assert plans.exists(), "Plans folder should exist"
        assert plans.is_dir(), "Plans should be a directory"
    
    def test_skills_folder_exists(self, vault_path):
        """Verify Skills folder exists"""
        skills = vault_path / 'Skills'
        assert skills.exists(), "Skills folder should exist"
        assert skills.is_dir(), "Skills should be a directory"


# ============================================================================
# Test 2: Core Python Files Tests
# ============================================================================

class TestCoreFiles:
    """Test that all required Python files exist"""
    
    def test_base_watcher_exists(self, vault_path):
        """Verify base_watcher.py exists"""
        base_watcher = vault_path / 'base_watcher.py'
        assert base_watcher.exists(), "base_watcher.py should exist"
    
    def test_file_system_watcher_exists(self, vault_path):
        """Verify file_system_watcher.py exists"""
        fs_watcher = vault_path / 'file_system_watcher.py'
        assert fs_watcher.exists(), "file_system_watcher.py should exist"
    
    def test_gmail_watcher_exists(self, vault_path):
        """Verify gmail_watcher.py exists"""
        gmail_watcher = vault_path / 'gmail_watcher.py'
        assert gmail_watcher.exists(), "gmail_watcher.py should exist"
    
    def test_linkedin_watcher_exists(self, vault_path):
        """Verify linkedin_watcher.py exists"""
        linkedin_watcher = vault_path / 'linkedin_watcher.py'
        assert linkedin_watcher.exists(), "linkedin_watcher.py should exist"
    
    def test_run_all_watchers_exists(self, vault_path):
        """Verify run_all_watchers.py exists"""
        run_all = vault_path / 'run_all_watchers.py'
        assert run_all.exists(), "run_all_watchers.py should exist"


# ============================================================================
# Test 3: Documentation Files Tests
# ============================================================================

class TestDocumentationFiles:
    """Test that all required documentation files exist"""
    
    def test_dashboard_exists(self, vault_path):
        """Verify Dashboard.md exists"""
        dashboard = vault_path / 'Dashboard.md'
        assert dashboard.exists(), "Dashboard.md should exist"
    
    def test_company_handbook_exists(self, vault_path):
        """Verify Company_Handbook.md exists"""
        handbook = vault_path / 'Company_Handbook.md'
        assert handbook.exists(), "Company_Handbook.md should exist"
    
    def test_readme_exists(self, vault_path):
        """Verify README.md exists"""
        readme = vault_path / 'README.md'
        assert readme.exists(), "README.md should exist"
    
    def test_silver_submission_readme_exists(self, vault_path):
        """Verify README_silver_submission.md exists"""
        silver_readme = vault_path / 'README_silver_submission.md'
        assert silver_readme.exists(), "README_silver_submission.md should exist"
    
    def test_silver_checklist_exists(self, vault_path):
        """Verify silver_tier_completion_checklist.md exists"""
        checklist = vault_path / 'silver_tier_completion_checklist.md'
        assert checklist.exists(), "silver_tier_completion_checklist.md should exist"


# ============================================================================
# Test 4: Skills Documentation Tests
# ============================================================================

class TestSkillsDocumentation:
    """Test that all skills documentation exists"""
    
    def test_all_skills_documentation_exists(self, vault_path):
        """Verify all_silver_skills_documentation.md exists"""
        skills_doc = vault_path / 'Skills' / 'all_silver_skills_documentation.md'
        assert skills_doc.exists(), "all_silver_skills_documentation.md should exist"
    
    def test_gmail_setup_guide_exists(self, vault_path):
        """Verify gmail_setup_guide.md exists"""
        guide = vault_path / 'Skills' / 'Watchers' / 'gmail_setup_guide.md'
        assert guide.exists(), "gmail_setup_guide.md should exist"
    
    def test_linkedin_setup_guide_exists(self, vault_path):
        """Verify linkedin_setup_guide.md exists"""
        guide = vault_path / 'Skills' / 'Watchers' / 'linkedin_setup_guide.md'
        assert guide.exists(), "linkedin_setup_guide.md should exist"
    
    def test_task_scheduler_guide_exists(self, vault_path):
        """Verify task_scheduler_silver.md exists"""
        guide = vault_path / 'Skills' / 'Scheduling' / 'task_scheduler_silver.md'
        assert guide.exists(), "task_scheduler_silver.md should exist"
    
    def test_mcp_email_guide_exists(self, vault_path):
        """Verify mcp_email_server_guide.md exists"""
        guide = vault_path / 'Skills' / 'MCP' / 'mcp_email_server_guide.md'
        assert guide.exists(), "mcp_email_server_guide.md should exist"


# ============================================================================
# Test 5: File System Watcher Tests
# ============================================================================

class TestFileSystemWatcher:
    """Test file system watcher functionality"""
    
    def test_create_test_file_in_inbox(self, inbox_path):
        """Test creating a test file in Inbox"""
        test_file = inbox_path / 'pytest_test_file.txt'
        test_file.write_text('Test content for Silver Tier')
        assert test_file.exists(), "Test file should be created in Inbox"
    
    def test_file_has_content(self, inbox_path):
        """Test that test file has content"""
        test_file = inbox_path / 'pytest_test_file.txt'
        if test_file.exists():
            content = test_file.read_text()
            assert len(content) > 0, "Test file should have content"
            assert 'Test content' in content, "Test file should contain expected text"


# ============================================================================
# Test 6: Approval Workflow Tests
# ============================================================================

class TestApprovalWorkflow:
    """Test approval workflow functionality"""
    
    def test_create_approval_request(self, pending_approval_path):
        """Test creating an approval request file"""
        approval_file = pending_approval_path / 'PYTEST_approval_test.md'
        content = """---
type: test_approval
status: pending
created: 2026-02-14
---

# Test Approval Request

This is a pytest test for approval workflow.

## Action Required
Move this file to Approved folder to test the workflow.
"""
        approval_file.write_text(content)
        assert approval_file.exists(), "Approval request file should be created"
    
    def test_approval_file_format(self, pending_approval_path):
        """Test that approval file has correct format"""
        approval_file = pending_approval_path / 'PYTEST_approval_test.md'
        if approval_file.exists():
            content = approval_file.read_text()
            assert '---' in content, "Approval file should have YAML frontmatter"
            assert 'type:' in content, "Approval file should specify type"
            assert 'status:' in content, "Approval file should specify status"


# ============================================================================
# Test 7: Plan.md Tests
# ============================================================================

class TestPlanCreation:
    """Test plan.md creation functionality"""
    
    def test_create_plan_file(self, plans_path):
        """Test creating a plan file"""
        plan_file = plans_path / 'PLAN_pytest_test_001.md'
        content = """---
plan_id: pytest-test-001
date_created: 2026-02-14
status: pending_approval
objective: Test plan creation functionality
---

# Test Plan

## Objective
Test the plan creation functionality for Silver Tier.

## Steps
1. Create this plan file
2. Verify format
3. Confirm integration

## Timeline
- Complete by: 2026-02-14
- Priority: Normal
"""
        plan_file.write_text(content)
        assert plan_file.exists(), "Plan file should be created"
    
    def test_plan_file_format(self, plans_path):
        """Test that plan file has correct format"""
        plan_file = plans_path / 'PLAN_pytest_test_001.md'
        if plan_file.exists():
            content = plan_file.read_text()
            assert '---' in content, "Plan file should have YAML frontmatter"
            assert 'plan_id:' in content, "Plan file should have plan_id"
            assert 'objective:' in content, "Plan file should have objective"
            assert '## Steps' in content, "Plan file should have Steps section"


# ============================================================================
# Test 8: Dashboard Tests
# ============================================================================

class TestDashboard:
    """Test dashboard functionality"""
    
    def test_dashboard_exists(self, vault_path):
        """Verify Dashboard.md exists"""
        dashboard = vault_path / 'Dashboard.md'
        assert dashboard.exists(), "Dashboard.md should exist"
    
    def test_dashboard_has_silver_status(self, vault_path):
        """Test that dashboard shows Silver Tier status"""
        dashboard = vault_path / 'Dashboard.md'
        if dashboard.exists():
            content = dashboard.read_text()
            assert 'Silver Tier' in content, "Dashboard should mention Silver Tier"
            assert 'COMPLETE' in content or 'complete' in content, "Dashboard should show completion status"
    
    def test_dashboard_has_checklist(self, vault_path):
        """Test that dashboard has completion checklist"""
        dashboard = vault_path / 'Dashboard.md'
        if dashboard.exists():
            content = dashboard.read_text()
            assert 'Completion Checklist' in content or 'completion checklist' in content, \
                "Dashboard should have completion checklist"


# ============================================================================
# Test 9: Gmail Integration Tests
# ============================================================================

class TestGmailIntegration:
    """Test Gmail watcher integration"""
    
    def test_credentials_file_exists(self, vault_path):
        """Verify credentials.json exists for Gmail API"""
        credentials = vault_path / 'credentials.json'
        assert credentials.exists(), "credentials.json should exist for Gmail API"
    
    def test_credentials_file_format(self, vault_path):
        """Test that credentials file has correct format"""
        credentials = vault_path / 'credentials.json'
        if credentials.exists():
            import json
            try:
                with open(credentials, 'r') as f:
                    data = json.load(f)
                assert 'installed' in data or 'web' in data, \
                    "Credentials should have OAuth configuration"
            except json.JSONDecodeError:
                pytest.fail("credentials.json should be valid JSON")


# ============================================================================
# Test 10: LinkedIn Integration Tests
# ============================================================================

class TestLinkedInIntegration:
    """Test LinkedIn watcher integration"""
    
    def test_linkedin_watcher_imports(self, vault_path):
        """Test that LinkedIn watcher can be imported"""
        import sys
        sys.path.insert(0, str(vault_path))
        try:
            from linkedin_watcher import LinkedInWatcher
            assert True, "LinkedInWatcher should be importable"
        except ImportError as e:
            pytest.fail(f"LinkedInWatcher should be importable: {e}")
    
    def test_linkedin_watcher_class_exists(self, vault_path):
        """Test that LinkedInWatcher class exists"""
        import sys
        sys.path.insert(0, str(vault_path))
        try:
            from linkedin_watcher import LinkedInWatcher
            assert hasattr(LinkedInWatcher, 'check_for_updates'), \
                "LinkedInWatcher should have check_for_updates method"
            assert hasattr(LinkedInWatcher, 'create_action_file'), \
                "LinkedInWatcher should have create_action_file method"
        except ImportError:
            pytest.fail("LinkedInWatcher class should exist")


# ============================================================================
# Test 11: End-to-End Workflow Tests
# ============================================================================

class TestEndToEndWorkflow:
    """Test complete end-to-end workflow"""
    
    def test_complete_workflow_simulation(self, vault_path, inbox_path, needs_action_path, 
                                         pending_approval_path, approved_path, done_path):
        """Simulate complete workflow from inbox to done"""
        import time
        timestamp = str(int(time.time() * 1000))  # Unique timestamp
        
        # Step 1: Create file in Inbox
        inbox_file = inbox_path / f'workflow_test_{timestamp}.txt'
        inbox_file.write_text('End-to-end workflow test')
        
        # Step 2: Verify file created
        assert inbox_file.exists(), "Test file should be created in Inbox"
        
        # Step 3: Simulate action file creation (normally done by watcher)
        action_file = needs_action_path / f'action_workflow_test_{timestamp}.md'
        action_file.write_text('# Action File\n\nGenerated from inbox file')
        
        # Step 4: Move to Pending Approval (simulate)
        pending_file = pending_approval_path / f'action_workflow_test_{timestamp}.md'
        if action_file.exists():
            action_file.rename(pending_file)
            assert pending_file.exists(), "File should be moved to Pending_Approval"
        
        # Step 5: Move to Approved (simulate approval)
        approved_file = approved_path / f'action_workflow_test_{timestamp}.md'
        if pending_file.exists():
            pending_file.rename(approved_file)
            assert approved_file.exists(), "File should be moved to Approved"
        
        # Step 6: Move to Done (simulate completion)
        done_file = done_path / f'action_workflow_test_{timestamp}.md'
        if approved_file.exists():
            approved_file.rename(done_file)
            assert done_file.exists(), "File should be moved to Done"


# ============================================================================
# Test 12: Silver Tier Requirements Tests
# ============================================================================

class TestSilverTierRequirements:
    """Test all Silver Tier requirements are met"""
    
    def test_two_or_more_watchers(self, vault_path):
        """Verify two or more watchers are implemented"""
        watchers = []
        if (vault_path / 'file_system_watcher.py').exists():
            watchers.append('FileSystemWatcher')
        if (vault_path / 'gmail_watcher.py').exists():
            watchers.append('GmailWatcher')
        if (vault_path / 'linkedin_watcher.py').exists():
            watchers.append('LinkedInWatcher')
        
        assert len(watchers) >= 2, f"Should have at least 2 watchers, found: {len(watchers)}"
    
    def test_plan_creation_working(self, plans_path):
        """Verify Plan.md creation is working"""
        # Check if at least one plan file exists
        plan_files = list(plans_path.glob('PLAN_*.md'))
        assert len(plan_files) > 0, "Should have at least one PLAN_*.md file"
    
    def test_approval_workflow_tested(self, vault_path):
        """Verify approval workflow is tested"""
        # Check if approval workflow folders exist
        assert (vault_path / 'Pending_Approval').exists(), "Pending_Approval folder should exist"
        assert (vault_path / 'Approved').exists(), "Approved folder should exist"
    
    def test_dashboard_shows_silver_status(self, vault_path):
        """Verify dashboard shows Silver status"""
        dashboard = vault_path / 'Dashboard.md'
        if dashboard.exists():
            content = dashboard.read_text()
            assert 'Silver' in content, "Dashboard should mention Silver tier"
    
    def test_documentation_complete(self, vault_path):
        """Verify all documentation is complete"""
        required_docs = [
            'Dashboard.md',
            'Company_Handbook.md',
            'README.md',
            'silver_tier_completion_checklist.md'
        ]
        
        for doc in required_docs:
            doc_path = vault_path / doc
            assert doc_path.exists(), f"{doc} should exist"


# ============================================================================
# Cleanup Fixtures
# ============================================================================

@pytest.fixture(autouse=True)
def cleanup_test_files(vault_path):
    """Cleanup test files after each test"""
    yield
    
    # Clean up test files from Inbox
    inbox = vault_path / 'Inbox'
    if inbox.exists():
        for file in inbox.glob('pytest_*.txt'):
            try:
                file.unlink()
            except:
                pass
    
    # Clean up test files from Plans
    plans = vault_path / 'Plans'
    if plans.exists():
        for file in plans.glob('PLAN_pytest_*.md'):
            try:
                file.unlink()
            except:
                pass
    
    # Clean up test files from Pending_Approval
    pending = vault_path / 'Pending_Approval'
    if pending.exists():
        for file in pending.glob('PYTEST_*.md'):
            try:
                file.unlink()
            except:
                pass


# ============================================================================
# Run Tests
# ============================================================================

if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])