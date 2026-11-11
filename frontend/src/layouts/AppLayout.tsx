import { Menu, X } from 'lucide-react'
import { useState } from 'react'
import { NavLink, Outlet, useLocation } from 'react-router-dom'
import { Logo } from '../components/ui/Logo'
import { StatusChip } from '../components/ui/StatusChip'
import { isApiConfigured } from '../config/env'
import { navItems } from '../routes/navigation'

export function AppLayout() {
  const [open, setOpen] = useState(false)
  const location = useLocation()
  const current = navItems.find((n) => location.pathname.endsWith(`/${n.path}`))

  const nav = (
    <nav aria-label="Main navigation" className="flex-1 overflow-y-auto px-3 py-4">
      <p className="num mb-2 px-3 text-[10px] uppercase tracking-[0.2em] text-ink-mute">Workspace</p>
      <div className="space-y-0.5">
        {navItems.map(({ path, label, icon: Icon }) => (
          <NavLink
            key={path}
            to={`/app/${path}`}
            onClick={() => setOpen(false)} // close the mobile menu after navigating
            className={({ isActive }) =>
              `group relative flex items-center gap-3 rounded px-3 py-2 text-sm font-medium transition-all duration-200 ${
                isActive
                  ? 'bg-primary/10 text-primary-light'
                  : 'text-ink-soft hover:translate-x-0.5 hover:bg-white/5 hover:text-ink'
              }`
            }
          >
            {({ isActive }) => (
              <>
                <span
                  aria-hidden
                  className={`absolute inset-y-1.5 left-0 w-0.5 rounded-full bg-primary shadow-[0_0_10px_rgba(16,185,129,0.9)] transition-all duration-300 ${
                    isActive ? 'scale-y-100 opacity-100' : 'scale-y-0 opacity-0'
                  }`}
                />
                <Icon size={17} aria-hidden className="transition-transform duration-200 group-hover:scale-110" />
                {label}
              </>
            )}
          </NavLink>
        ))}
      </div>
    </nav>
  )

  const apiChip = (
    <StatusChip tone={isApiConfigured ? 'emerald' : 'amber'} live>
      {isApiConfigured ? 'API connected' : 'API not connected'}
    </StatusChip>
  )

  return (
    <div className="min-h-screen lg:flex">
      {/* Desktop sidebar */}
      <aside className="sticky top-0 hidden h-screen w-64 shrink-0 flex-col border-r border-white/5 bg-deep lg:flex">
        <div className="border-b border-white/5 px-5 py-4">
          <NavLink to="/">
            <Logo />
          </NavLink>
        </div>
        {nav}
        <div className="border-t border-white/5 p-4">{apiChip}</div>
      </aside>

      {/* Mobile top bar */}
      <header className="sticky top-0 z-30 flex items-center justify-between border-b border-white/5 bg-deep/90 px-4 py-3 backdrop-blur lg:hidden">
        <NavLink to="/">
          <Logo />
        </NavLink>
        <button type="button" onClick={() => setOpen(true)} aria-label="Open menu" className="btn btn-ghost !px-2">
          <Menu size={22} />
        </button>
      </header>

      {/* Mobile drawer */}
      {open && (
        <div className="fixed inset-0 z-40 lg:hidden" role="dialog" aria-modal="true" aria-label="Menu">
          <button type="button" aria-label="Close menu" className="absolute inset-0 bg-black/70 backdrop-blur-sm" onClick={() => setOpen(false)} />
          <div className="drawer-in absolute inset-y-0 left-0 flex w-72 max-w-[85%] flex-col border-r border-white/5 bg-deep">
            <div className="flex items-center justify-between border-b border-white/5 px-5 py-4">
              <Logo />
              <button type="button" onClick={() => setOpen(false)} aria-label="Close menu" className="p-1 text-ink-soft">
                <X size={20} />
              </button>
            </div>
            {nav}
            <div className="border-t border-white/5 p-4">{apiChip}</div>
          </div>
        </div>
      )}

      <div className="min-w-0 flex-1">
        {/* Desktop status bar */}
        <div className="hidden items-center justify-between border-b border-white/5 px-8 py-3 lg:flex">
          <p className="num text-xs uppercase tracking-[0.18em] text-ink-mute">
            FH <span className="text-ink-mute/60">/</span> <span className="text-ink-soft">{current?.label ?? 'Workspace'}</span>
          </p>
          <div className="flex items-center gap-2">
            <StatusChip tone="neutral">No market data loaded</StatusChip>
            {apiChip}
          </div>
        </div>

        <main className="mx-auto max-w-[1600px] px-4 py-8 sm:px-6 lg:px-8">
          {/* key re-runs the entrance animation on every page change */}
          <div key={location.pathname}>
            <Outlet />
          </div>
          <p className="mt-12 border-t border-white/5 pt-4 text-xs text-ink-mute">
            Financial Harness provides analysis for information only. It is not financial advice. Simulated results are not guaranteed
            returns.
          </p>
        </main>
      </div>
    </div>
  )
}
