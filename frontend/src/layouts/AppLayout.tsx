import { Menu, X } from 'lucide-react'
import { useState } from 'react'
import { NavLink, Outlet } from 'react-router-dom'
import { Logo } from '../components/ui/Logo'
import { navItems } from '../routes/navigation'

export function AppLayout() {
  const [open, setOpen] = useState(false)

  const nav = (
    <nav aria-label="Main navigation" className="flex-1 space-y-1 overflow-y-auto px-3 py-4">
      {navItems.map(({ path, label, icon: Icon }) => (
        <NavLink
          key={path}
          to={`/app/${path}`}
          onClick={() => setOpen(false)} // close the mobile menu after navigating
          className={({ isActive }) =>
            `flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors ${
              isActive ? 'bg-brand-600 text-white' : 'text-ink-300 hover:bg-navy-700 hover:text-ink-100'
            }`
          }
        >
          <Icon size={18} aria-hidden />
          {label}
        </NavLink>
      ))}
    </nav>
  )

  return (
    <div className="min-h-screen lg:flex">
      {/* Desktop sidebar */}
      <aside className="sticky top-0 hidden h-screen w-64 shrink-0 flex-col border-r border-navy-600/60 bg-navy-950 lg:flex">
        <div className="border-b border-navy-600/60 px-5 py-4">
          <NavLink to="/">
            <Logo />
          </NavLink>
        </div>
        {nav}
      </aside>

      {/* Mobile top bar */}
      <header className="sticky top-0 z-30 flex items-center justify-between border-b border-navy-600/60 bg-navy-950 px-4 py-3 lg:hidden">
        <NavLink to="/">
          <Logo />
        </NavLink>
        <button
          type="button"
          onClick={() => setOpen(true)}
          aria-label="Open menu"
          className="rounded-lg p-2 text-ink-300 hover:bg-navy-700"
        >
          <Menu size={22} />
        </button>
      </header>

      {/* Mobile drawer */}
      {open && (
        <div className="fixed inset-0 z-40 lg:hidden" role="dialog" aria-modal="true" aria-label="Menu">
          <button
            type="button"
            aria-label="Close menu"
            className="absolute inset-0 bg-black/60"
            onClick={() => setOpen(false)}
          />
          <div className="absolute inset-y-0 left-0 flex w-72 max-w-[85%] flex-col bg-navy-950">
            <div className="flex items-center justify-between border-b border-navy-600/60 px-5 py-4">
              <Logo />
              <button type="button" onClick={() => setOpen(false)} aria-label="Close menu" className="p-1 text-ink-300">
                <X size={20} />
              </button>
            </div>
            {nav}
          </div>
        </div>
      )}

      <main className="min-w-0 flex-1 px-4 py-6 sm:px-6 lg:px-8">
        <Outlet />
        <p className="mt-10 border-t border-navy-600/60 pt-4 text-xs text-ink-500">
          Financial Harness provides analysis for information only. It is not financial advice. Simulated results are
          not guaranteed returns.
        </p>
      </main>
    </div>
  )
}
