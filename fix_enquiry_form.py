enquiry_modal_html = '''
    <!-- ENQUIRY SUBMISSION SUCCESS MODAL -->
    <div id="enquiry-modal" class="fixed inset-0 z-50 hidden bg-zinc-950/90 backdrop-blur-xl flex items-center justify-center p-4 sm:p-6 no-print" onclick="handleEnquiryModalBackdrop(event)">
        <div class="max-w-lg w-full glass-panel rounded-3xl p-6 sm:p-8 border border-amber-500/40 text-white relative shadow-2xl space-y-6 animate-fade-in" onclick="event.stopPropagation()">
            
            <!-- Header -->
            <div class="flex items-start justify-between border-b border-zinc-800 pb-4">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                    </div>
                    <div>
                        <span class="text-[10px] uppercase tracking-widest text-amber-400 font-semibold block">Booking Desk</span>
                        <h3 class="font-serif text-2xl font-bold text-white">Enquiry Draft Prepared!</h3>
                    </div>
                </div>
                <button onclick="closeEnquiryModal()" class="p-2 rounded-full bg-zinc-800 hover:bg-zinc-700 text-zinc-400 hover:text-white transition-colors cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>

            <!-- Body Message -->
            <p class="text-xs text-zinc-300 leading-relaxed">
                Your shoot details have been drafted for Cameron Harding. Choose your preferred method to send:
            </p>

            <!-- Send Action Buttons -->
            <div class="space-y-3">
                <!-- Gmail Web Button -->
                <a id="enquiry-gmail-btn" href="#" target="_blank" class="w-full py-3.5 px-4 rounded-xl bg-amber-500 hover:bg-amber-400 text-zinc-950 font-semibold text-xs uppercase tracking-widest transition-all shadow-lg flex items-center justify-center space-x-2.5 cursor-pointer">
                    <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/></svg>
                    <span>Send via Gmail Web</span>
                </a>

                <!-- Default Mail App Button -->
                <a id="enquiry-mailto-btn" href="#" class="w-full py-3.5 px-4 rounded-xl bg-zinc-900 hover:bg-zinc-800 border border-zinc-700 hover:border-amber-400/50 text-white font-semibold text-xs uppercase tracking-widest transition-all flex items-center justify-center space-x-2.5 cursor-pointer">
                    <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                    <span>Open Default Mail App (Outlook / Apple Mail)</span>
                </a>

                <!-- Copy to Clipboard Button -->
                <button onclick="copyEnquiryToClipboard()" class="w-full py-3 px-4 rounded-xl bg-zinc-900/60 hover:bg-zinc-800 border border-zinc-800 text-zinc-300 hover:text-white text-xs uppercase tracking-wider transition-all flex items-center justify-center space-x-2 cursor-pointer">
                    <svg class="w-4 h-4 text-zinc-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path></svg>
                    <span id="copy-btn-label">Copy Brief to Clipboard</span>
                </button>
            </div>

            <!-- Direct Contact Footer inside Modal -->
            <div class="pt-4 border-t border-zinc-800/80 flex items-center justify-between text-[11px] text-zinc-400">
                <span>Direct Desk:</span>
                <a href="mailto:cameronhardingmodel@gmail.com" class="text-amber-400 font-semibold hover:underline">cameronhardingmodel@gmail.com</a>
            </div>

        </div>
    </div>

    <!-- TOAST NOTIFICATION CONTAINER -->
    <div id="toast-notification" class="fixed bottom-6 right-6 z-50 transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none">
        <div class="glass-panel px-5 py-3 rounded-2xl border border-amber-500/50 shadow-2xl flex items-center space-x-3 text-white">
            <span class="w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
            <span id="toast-message" class="text-xs font-medium tracking-wide"></span>
        </div>
    </div>
'''

enquiry_js = '''
        // Toast Notification System
        function showToast(message, duration = 3000) {
            const toast = document.getElementById('toast-notification');
            const msgEl = document.getElementById('toast-message');
            if (!toast || !msgEl) return;
            
            msgEl.innerText = message;
            toast.classList.remove('translate-y-20', 'opacity-0', 'pointer-events-none');
            toast.classList.add('translate-y-0', 'opacity-100');
            
            setTimeout(() => {
                toast.classList.remove('translate-y-0', 'opacity-100');
                toast.classList.add('translate-y-20', 'opacity-0', 'pointer-events-none');
            }, duration);
        }

        // Enquiry Modal Handlers
        let draftedEnquiryText = '';

        function openEnquiryModal() {
            const modal = document.getElementById('enquiry-modal');
            if (modal) {
                modal.classList.remove('hidden');
                document.body.style.overflow = 'hidden';
            }
        }

        function closeEnquiryModal() {
            const modal = document.getElementById('enquiry-modal');
            if (modal) {
                modal.classList.add('hidden');
                document.body.style.overflow = 'auto';
            }
        }

        function handleEnquiryModalBackdrop(e) {
            if (e.target.id === 'enquiry-modal') {
                closeEnquiryModal();
            }
        }

        function copyEnquiryToClipboard() {
            if (!draftedEnquiryText) return;
            navigator.clipboard.writeText(draftedEnquiryText).then(() => {
                const label = document.getElementById('copy-btn-label');
                if (label) {
                    const original = label.innerText;
                    label.innerText = '✓ Copied to Clipboard!';
                    showToast('Brief copied to clipboard!');
                    setTimeout(() => { label.innerText = original; }, 2500);
                }
            }).catch(() => {
                showToast('Unable to copy automatically.');
            });
        }

        function handleFormSubmit(e) {
            e.preventDefault();
            const name = document.getElementById('form-name').value.trim();
            const email = document.getElementById('form-email').value.trim();
            const category = document.getElementById('form-category').value;
            const location = document.getElementById('form-location').value.trim() || 'Not specified';
            const message = document.getElementById('form-message').value.trim();

            if (!name || !email || !message) {
                showToast('Please fill out all required fields.');
                return;
            }

            const subject = `Booking Enquiry: ${category} - ${name}`;
            const body = 
                `Hi Cameron,\\n\\n` +
                `I am contacting you regarding a modeling booking enquiry:\\n\\n` +
                `Client / Agency: ${name}\\n` +
                `Contact Email: ${email}\\n` +
                `Booking Category: ${category}\\n` +
                `Location & Date: ${location}\\n\\n` +
                `Project Brief / Details:\\n${message}\\n\\n` +
                `Best regards,\\n${name}`;

            draftedEnquiryText = `Subject: ${subject}\\n\\n${body}`;

            const encodedSubject = encodeURIComponent(subject);
            const encodedBody = encodeURIComponent(body);

            const mailtoUrl = `mailto:cameronhardingmodel@gmail.com?subject=${encodedSubject}&body=${encodedBody}`;
            const gmailUrl = `https://mail.google.com/mail/?view=cm&fs=1&to=cameronhardingmodel@gmail.com&su=${encodedSubject}&body=${encodedBody}`;

            // Update links in modal
            const mailtoBtn = document.getElementById('enquiry-mailto-btn');
            const gmailBtn = document.getElementById('enquiry-gmail-btn');
            if (mailtoBtn) mailtoBtn.href = mailtoUrl;
            if (gmailBtn) gmailBtn.href = gmailUrl;

            // Show Toast & Open Modal
            showToast('Drafting enquiry for Cameron Harding...');
            openEnquiryModal();

            // Also attempt to trigger default mail client directly
            try {
                window.location.href = mailtoUrl;
            } catch (err) {
                console.log('Direct mailto opening:', err);
            }
        }
'''

import re

for filepath in ['index.html', 'index_external.html', 'portfolio_standalone.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean out any old enquiry modal if present
    if 'id="enquiry-modal"' in content:
        content = re.sub(r'<!-- ENQUIRY SUBMISSION SUCCESS MODAL -->.*?<!-- TOAST NOTIFICATION CONTAINER -->.*?</div>\s*</div>', '', content, flags=re.DOTALL)

    # 2. Inject enquiry modal right before </main>
    if 'id="enquiry-modal"' not in content:
        content = content.replace('</main>', enquiry_modal_html + '\n    </main>')

    # 3. Replace handleFormSubmit with new comprehensive implementation
    # Match from "function handleFormSubmit" to the end of handleFormSubmit
    old_fn_pattern = r'function handleFormSubmit\(e\)\s*\{.*?window\.location\.href\s*=\s*`mailto:[^`]+`;\s*\}'
    if re.search(old_fn_pattern, content, re.DOTALL):
        content = re.sub(old_fn_pattern, enquiry_js.strip(), content, flags=re.DOTALL)
    elif 'function handleFormSubmit(e)' in content:
        # Fallback replacement
        start = content.find('function handleFormSubmit(e)')
        end = content.find('// Close modal on Escape key', start)
        if end != -1:
            content = content[:start] + enquiry_js.strip() + '\n\n        ' + content[end:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath} with interactive enquiry modal & working form submit handler!")
