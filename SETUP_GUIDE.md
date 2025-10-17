# CML Job Monitor - n8n Setup Guide

## Overview
This workflow monitors your CML jobs every 5 minutes and sends email notifications when jobs succeed or fail.

## Prerequisites
- n8n installed and running on CML
- CML API key
- SMTP email credentials configured in n8n

## Setup Instructions

### Step 1: Get Your CML API Key
1. Go to: https://ml-691d78db-049.se-sandb.a465-9q4k.cloudera.site/
2. Click on your profile (top right)
3. Go to **User Settings** → **API Keys**
4. Click **Create API Key**
5. Copy the key (you'll need it in Step 3)

### Step 2: Configure SMTP in n8n
1. In n8n, go to **Credentials** → **Add Credential**
2. Search for **SMTP**
3. Enter your email settings:
   - **User**: your-email@example.com
   - **Password**: your-email-password
   - **Host**: smtp.gmail.com (or your SMTP server)
   - **Port**: 587
   - **SSL/TLS**: Enable
4. Click **Save**

### Step 3: Import the Workflow
1. In n8n, click **Workflows** → **Add Workflow** → **Import from File**
2. Upload: `cml_job_monitor_workflow.json`
3. The workflow will open in the editor

### Step 4: Configure the Workflow

#### A. Update API Key (2 nodes need this)
**Node 1: "Get CML Jobs"**
- Click the node
- Find the Authorization header
- Replace `YOUR_CML_API_KEY_HERE` with your actual API key from Step 1

**Node 2: "Get Latest Job Run"**
- Click the node
- Find the Authorization header
- Replace `YOUR_CML_API_KEY_HERE` with your actual API key from Step 1

#### B. Configure Email Nodes (2 nodes need this)
**Node 3: "Email Success"**
- Click the node
- Select your SMTP credential from the dropdown
- Update **From Email**: your-email@example.com
- Update **To Email**: recipient@example.com

**Node 4: "Email Failure"**
- Click the node
- Select your SMTP credential from the dropdown
- Update **From Email**: your-email@example.com
- Update **To Email**: recipient@example.com

### Step 5: Test the Workflow

#### Manual Test (Recommended First)
1. **Disable the schedule trigger** (so it doesn't run every 5 minutes during testing)
   - Click "Every 5 Minutes" node
   - Toggle the **Active** switch to OFF
2. Click **"Execute Workflow"** button (top right)
3. Watch the nodes execute in sequence
4. Check your email for notifications

#### Test Your Demo Jobs
1. Go to CML and manually run your test jobs:
   - `success_job.py`
   - `failure_job.py`
   - `slow_job.py`
2. Wait for them to complete
3. Run the n8n workflow again
4. Verify you receive the appropriate emails

### Step 6: Enable Automatic Monitoring
Once testing is complete:
1. Click the **"Every 5 Minutes"** node
2. Toggle **Active** to ON
3. Click **Save** at the top
4. The workflow will now run automatically every 5 minutes

### Step 7: Disable After Demo
To stop the monitoring after your demo:
1. Click the **"Every 5 Minutes"** node
2. Toggle **Active** to OFF
3. Click **Save**

## Workflow Nodes Explained

```
Every 5 Minutes (Schedule Trigger)
  ↓
Get CML Jobs (HTTP Request)
  → Fetches all jobs in your project
  ↓
Extract Jobs Array (Set)
  → Pulls out the jobs array from response
  ↓
Split Into Items (Split Out)
  → Creates one item per job for processing
  ↓
Get Latest Job Run (HTTP Request)
  → For each job, gets its most recent run
  ↓
Format Job Data (Set)
  → Extracts relevant fields (name, status, times)
  ↓
Check If Success (IF node)
  → Routes to success or failure branch
  ↓
Email Success / Email Failure
  → Sends formatted email notification
```

## Troubleshooting

### Issue: "401 Unauthorized" error
**Solution**: Check your API key is correct and properly formatted as `Bearer YOUR_KEY`

### Issue: No emails received
**Solution**: 
- Verify SMTP credentials are correct
- Check spam folder
- Test SMTP settings in n8n credentials

### Issue: "No job_runs found" error
**Solution**: Make sure your jobs have been run at least once

### Issue: Workflow runs but shows no data
**Solution**: 
- Verify project ID is correct: `56ux-3674-1e1k-32bk`
- Check that jobs exist in the project
- Manually test the API URL in a browser or Postman

## Customization Options

### Change Polling Frequency
1. Click "Every 5 Minutes" node
2. Change `minutesInterval` value (e.g., 1, 10, 15)

### Add More Status Checks
Currently checks for "succeeded" vs anything else. To add specific handling for "stopped" or "running":
1. Click "Check If Success" node
2. Add more conditions

### Customize Email Templates
1. Click "Email Success" or "Email Failure" nodes
2. Edit the `message` field (supports HTML)

## Testing Checklist
- [ ] API key configured in both HTTP nodes
- [ ] SMTP credentials configured
- [ ] Email addresses updated
- [ ] Manual execution successful
- [ ] Received success email for successful job
- [ ] Received failure email for failed job
- [ ] Schedule trigger disabled after testing

## Next Steps
Once this basic workflow is working, you can extend it to:
- Store job history in a database
- Send Slack notifications instead of email
- Create dashboards showing job trends
- Auto-retry failed jobs
- Escalate repeated failures
