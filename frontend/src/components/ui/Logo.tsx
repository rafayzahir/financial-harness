export function Logo({ className = '' }: { className?: string }) {
  return (
    <span className={`inline-flex items-center gap-2.5 whitespace-nowrap font-display font-semibold tracking-tight text-ink ${className}`}>
      <span
        className="grid size-8 place-items-center rounded border border-primary/40 bg-primary/10 shadow-[0_0_18px_-4px_rgba(16,185,129,0.6)]"
        aria-hidden
      >
        <svg viewBox="0 0 24 24" className="size-5" fill="none" stroke="#34d399" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round">
          <path d="M3 17 9 11l4 3 8-9" />
        </svg>
      </span>
      <span>Financial Harness</span>
    </span>
  )
}
